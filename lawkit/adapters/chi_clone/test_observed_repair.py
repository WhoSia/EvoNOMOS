"""Compiler negative controls on a native-run manifest and witness checks."""
import copy
import json
from pathlib import Path
import sys
from observed_repair import compile_model


def test(root):
    spec=json.loads((root/'manifest.json').read_text())
    m=compile_model(spec,root)
    assert m['edges']==[['base','local','app',9],['base','shallow','upstream',2],
                       ['base','merged','upstream',27],['shallow','merged','upstream',29]]
    assert m['states']['local']['goals']==['public']
    assert m['states']['merged']['goals']==['public','full']
    assert not m['states']['shallow']['goals']
    def reject(change):
        s=copy.deepcopy(spec);change(s)
        try: compile_model(s,root)
        except (ValueError,KeyError,OSError): return
        raise AssertionError('invalid evidence accepted')
    reject(lambda s:s['snapshots']['base']['files']['context.go'].update(blob='0'*40))
    reject(lambda s:s['snapshots']['base']['observations'].pop('legacy'))
    reject(lambda s:s['snapshots']['base']['observations'].update(legacy=1))
    reject(lambda s:s['snapshots']['base']['files']['context.go'].update(file='../base.go'))
    reject(lambda s:s['transitions'].append(['local','merged']))
    reject(lambda s:s['transitions'].append(['base','base']))
    s=copy.deepcopy(spec);s['snapshots']['local']['observations']['legacy']=False
    assert not compile_model(s,root)['states']['local']['safe']
    print('PASS six rejection controls, unsafe-state preservation and observed graph')


if __name__=='__main__':
    test(Path(sys.argv[1]))
