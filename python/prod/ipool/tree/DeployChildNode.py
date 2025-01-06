from ..tree.TreeNode import TreeNode

class DeployChildNode:

    def __init__(self, parent_node):
        self.parent = parent_node

    def apply(self, lp):
        child_node = TreeNode(lp)
        self.parent.add_child(child_node)
        return child_node

    def init_liquidity(self, child_node, token_in, recipient, amount_in):

        if(self._is_synth_node(child_node)):
            return self._synth(child_node, token_in, recipient, amount_in)
        else:
            return self._hybrid(child_node, token_in, recipient, amount_in)
            
    def _hybrid(self, child_node, token_in, recipient, amount_in):
        is_tkn0 = token_in.token_name == child_node.lp.mm.x_tkn.token_name
        is_tkn1 = token_in.token_name == child_node.lp.mm.y_tkn.token_name
        assert is_tkn0 or is_tkn1, 'PachiraV1: DEPLOYMENT_TOKEN_UNAVAILABLE' 

        child_nm = child_node.lp.base_lp.name
        lp = self.parent.child[child_nm].lp.base_lp
        
        amount_in0, amount_in1 = self._split_amt(amount_in)
        token_in_amt = amount_in0 if is_tkn0 else amount_in1
        base_in_amt = amount_in1 if is_tkn0 else amount_in0
        op_token_in_amt = self.parent.lp.exchangein_basein_yieldout(token_in, lp, base_in_amt, recipient)
        
        amt_tkn0_add = token_in_amt if is_tkn0 else op_token_in_amt
        amt_tkn1_add = op_token_in_amt if is_tkn0 else token_in_amt
        lp.add_liquidity(recipient, amt_tkn0_add, amt_tkn1_add, amt_tkn0_add, amt_tkn1_add)

        return lp.last_liquidity_deposit

    def _synth(self, child_node, token_in, recipient, amount_in):

        child_nm = child_node.lp.base_lp.name
        lp = self.parent.child[child_nm].lp.base_lp
        
        yield_in_amt = self.parent.lp.exchangein_basein_yieldout(token_in, lp, amount_in, recipient)
        
        amt_tkn0_add, amt_tkn1_add = self._split_amt(yield_in_amt)
        lp.add_liquidity(recipient, amt_tkn0_add, amt_tkn1_add, amt_tkn0_add, amt_tkn1_add)

        return lp.last_liquidity_deposit

    def _split_amt(self, yield_in):
        amt0 = yield_in//2
        amt1 = yield_in//2 
        amt0 = amt0 if amt0 + amt1 == yield_in else amt0 + 1
        return amt0, amt1

    def _is_synth_node(self, child_node):
        tkn0_type = child_node.lp.mm.x_tkn.type
        tkn1_type = child_node.lp.mm.y_tkn.type    
        return (tkn0_type == 'index') and (tkn1_type == 'index')