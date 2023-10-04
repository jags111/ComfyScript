import re

# TODO: PrimitiveNode
# TODO: Switch nodes: ModelMergeSimple, CRLoadLoRA, TomePatchModel, CLIPSetLastLayer, CRModelInputSwitch

def reroute_elimination(v, args, vars, c):
    if v.type != 'Reroute':
        return c
    assert re.fullmatch(r'(?:# )?(?:_ = Reroute\(\S+\)|(\S+) = Reroute\(\1\))\s*', c), c
    return ''

__all__ = [
    'reroute_elimination',
]