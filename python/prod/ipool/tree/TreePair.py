class TreePair:

    def __init__(self, tree_base):
        self.tree_base = tree_base

    def basein_tree_yieldout(self, child_node, token_in, token_out, recipient, amount_in):
    
        synth_tkn = self._retrieve_synth_token(child_node, token_in)
        synth_amt_out = self.tree_base.lp.exchangein_basein_synthout(token_in, synth_tkn, amount_in, recipient)
        synth_tkn.transfer(recipient, synth_amt_out)
        
        tree_yield_amt = child_node.lp.exchangein_basein_yieldout(synth_tkn, token_out, synth_amt_out, recipient)
        return tree_yield_amt
    
    def tree_yieldin_baseout(self, child_node, token_in, token_out, recipient, amount_in):
    
        synth_tkn = self._retrieve_synth_token(child_node, token_out)
        base_synth_amt_out = child_node.lp.exchangein_yieldin_baseout(token_in, synth_tkn, amount_in, recipient)
        
        base_amt_out = self.tree_base.lp.exchangein_synthin_baseout(synth_tkn, token_out, base_synth_amt_out, recipient)
        return base_amt_out

    def _retrieve_synth_token(self, child_node, token_in):
    
        lp = child_node.lp.base_lp
        tokens = lp.factory.token_from_exchange[lp.name]
        x_tkn = tokens[[*tokens][0]]
        y_tkn = tokens[[*tokens][1]]
    
        synth_tkn = None
        if y_tkn.type == 'index':
            if y_tkn.parent_tkn.token_name == token_in.token_name:
                synth_tkn = y_tkn
        if(x_tkn.type == 'index'):
            if x_tkn.parent_tkn.token_name == token_in.token_name:
                synth_tkn = x_tkn
    
        return synth_tkn
