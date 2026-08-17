# HKD∞ OBFUSCATE v3 — PYTHON-3.4-COMPATIBLE PROTECTED MODULE
# Source payload; no marshal/code-object version dependency.
# All protection work occurs once at import; protected calls have no wrapper.
import hashlib as _hh
import zlib as _hz

_B=(bytes.fromhex('aa72ab16e72a51212083ed8431074e8ad5ffd79c42c1963925f4e21302709169b2074f44e9b535f4773f9a3290eb4cbacc3f62615518f6edf3ee3fdbec53583793004c0d7620d4f4d9f5a632690644a7bb6b2a31c89c66fce3911b09ffb4b2949c82e2ff2fa4ceed7a0e53af2d525d97ca834c3908'),)
_I=(0,)
_L=(bytes.fromhex('efb5667dc4a33a76f3dee9d9aab52483b362ea203c4b30f7b1ea48ce5ae43838'),)
_R=bytes.fromhex('efb5667dc4a33a76f3dee9d9aab52483b362ea203c4b30f7b1ea48ce5ae43838')
_S1=bytes.fromhex('b4c44a1d49f84630e6a3d8f9e940b5fe9bac91bad310595a9d955dd8b13e68ff')
_S2=bytes.fromhex('7e50262985a1f8adbb970e2cb7aaab9a1c50293fd48e23303c28fc9662bd3098')

def _x(a,b):
    return bytes(i^j for i,j in zip(a,b))

def _n4(n):
    return n.to_bytes(4,'big')

def _ks(k,idx,n):
    o=bytearray(); c=0; s=k+_n4(idx)
    while len(o)<n:
        o.extend(_hh.sha256(s+_n4(c)).digest()); c+=1
    return bytes(o[:n])

def _mr(v):
    if not v:
        return _hh.sha256(b'').digest()
    v=list(v)
    while len(v)>1:
        if len(v)&1: v.append(v[-1])
        v=[_hh.sha256(v[i]+v[i+1]).digest() for i in range(0,len(v),2)]
    return v[0]

_K=_x(_S1,_S2)
_P=[]
_V=[]
for _i in range(len(_I)):
    _m=_B[_I[_i]]
    _r=_x(_m,_ks(_K,_i,len(_m)))
    _P.append(_r)
    _V.append(_hh.sha256(_n4(_i)+_r).digest())
if tuple(_V)!=_L or _mr(_V)!=_R:
    raise ImportError('HKD∞ SHA-256 integrity verification failed')

try:
    _S=_hz.decompress(b''.join(_P)).decode('utf-8')
except (ValueError, UnicodeDecodeError, _hz.error):
    raise ImportError('HKD∞ protected payload reconstruction failed')

_G=globals()
_N={
    '__name__':_G.get('__name__'),
    '__doc__':_G.get('__doc__'),
    '__package__':_G.get('__package__'),
    '__loader__':_G.get('__loader__'),
    '__spec__':_G.get('__spec__'),
    '__file__':_G.get('__file__'),
    '__cached__':_G.get('__cached__'),
    '__builtins__':_G.get('__builtins__'),
}
_C=compile(_S,_G.get('__file__') or '<HKD-obfuscated>','exec',0,True,0)
exec(_C,_N,_N)

for _q,_v in list(_N.items()):
    if _q != '__builtins__':
        _G[_q]=_v

# Functions retain _N as their normal globals dictionary. Remove loader-only names
# from the actual module namespace without mutating _N after source execution.
del _B,_I,_L,_R,_S1,_S2,_K,_P,_V,_S,_C,_i,_m,_r,_x,_n4,_ks,_mr,_q,_v,_N,_G,_hh,_hz
