# -*- coding: utf-8 -*-
# HKD OBFUSCATE v4 - portable source payload, no marshal/code-object dependency.
# Protection is import-time only; protected functions have no per-call wrapper.
def _hkd_v4_bootstrap(_g):
    import binascii as _hb
    import hashlib as _hh
    import struct as _hs
    import zlib as _hz

    _b = (
        _hb.unhexlify('d57f6ca83ba3f4bad724904d2550f74263d0baeabfe3172054255f20278ba85c6b7454622f4620cd31c76abe15992b09f0bb385b521553bfc22ce07a0c902bd67f776a3a7e479e73d07e73b370377a05b03d8013486107991404df8259ad55217c1bcef90aa16102ee450f4d3048ca70433d96a058b7f71ad144e4ca9b891a74'),
        _hb.unhexlify('923072b3d2ec67be603a5992b3c3c5859420feefd222406873e43d271eb62c5fe1fd0b1c09fdde1c5a4bd11ea09defe89eaf388f3f4477da6d480f621ac7c2b6608a5943056435dd30bf3711f2ca95de80d4253b3747f97c427f05374915bc2bf18790bb28e118910b7d88a8'),
        _hb.unhexlify('efe38d73f066d6c4c0efe63ccef2ecd7902cc11bea25a636e18b275f1824157b3fa6878ecab4bb01a62f7aa195271a66218ef6337d2039420c12ce2e62ce46cfe561e6e429993dd1e6bfaa2af84034804c5ebbca89a82676ec26d3bb96e04f79257ae19e02beb3daa590f049f03f0ef5109d0ec4e8b2663661816966b321cff0'),
        _hb.unhexlify('da6e5a9b62971994be79f3ae5ba02cbc449af8783da7ce156ee90c0cbc18d48aa09b872dcfc7e8f38f69d1e8fda91e59bf2372cc38c6144b3f4961929d4f8d7e105e5702bd470c74990809435dbdfa2ac427f6c719957b28a98d6b0b944451018830a7d93306f83dc8f7598d89acd1cf02b0b64243c780871bfee54c671d0cd4'),
        _hb.unhexlify('bceb4a1423eb97db46714fbbed7030c01f5ce2190a093234eb94ce125f6fc147eb7d838d7a5ce9f88686e9f5c8847996a84c5b9b214d507f4885849484b95bd9713a38f8e4e84afc38ecf1f305f0b7377c43f5c81b721c051b4073730b692c058453b6624b2a0284e949d8d4b0c9af8106d7d7eb7bbd5ec560931def37eb86cf'),
        _hb.unhexlify('a469ab617d3004fa9ca85b3d6cfd6d13b6da1b41c0c13358cf36e15dd984bb6b0376985125937201e344a9cfeb180a71aef098d3461a7fbf41de67e6aef466674bf7b7c985f8ff32da4f6f24ed975eae1538c9ccda56502720ec06d01d351c2ef1c2dddfc774d7705e675acb236fbee8759a7042c550135dfd70564558a43cab'),
        _hb.unhexlify('9dd9b430b31edb305e227552f59693c33e749bd46716e3e81e3e4d9ace41694b6ed41dc650ed5093bcca59cd9e306ef57d3ff7cd654161e3208c4950e4e26272a583f260021ad48cb8d97ae34f38ce0e95e4afa0de5737233059c79620e4992176a6c36da03b8ee5d122fe046a6257630ac7270c185a21660908a16eb22ce933'),
        _hb.unhexlify('6be99c0093bde2ce3bbf27b5a01169d8c6c9942a41a7b8e5c78441c7aa19651974d7852f5433bcb7f93929b559c1586ebf64d2f71f4b2584adea8828796398a891bb8e1268d16dad6eef122fc887d8e08b8d46655881ff1c9e1957b8e42f33675236335eeab1d359e839e36b6b0e5e81eea12f1cec941c0c95e33b900ded7f97'),
        _hb.unhexlify('1e2878ba899591b4ff16b2159ed833ce0246602f786af9297c52580c18a7261956edf79720ee3b42d925361da084e36e240a8c01b7fbc5c5997fdfef2f92a87bdd578cd4c0476c777f72642fdc297b0f93dba996e2f6eafb7e7f61285c7f1bb50714b9a2a13cf4eb96032c64e37b4e7fae46c845c1c4d498c42f2c1858c60a27'),
        _hb.unhexlify('6f4151ca79d5a5d13e7c3cddcbe65c9729a5316581b3f2c49924a517356d885441aa6ec0096720174dcbdc5b1485e41433acb07a5823bf65733176f248112d4ab6983a058e384438e018911f7d4426ec3fd329c0546e51f8113c284db0181ba94c9dae3d08e52dca7d116b5ff817d09cefe336143bc05f93b08f7dbf6e58d571'),
        _hb.unhexlify('8bb55aa4978c3412c4f1ea154973c9ccdfc604c862674d336e59d85e97b7c72815c3a0a6f5ead73b41046b67e40b1df0b769084a4cf5e58235dcd4aa18159d48233b76b09c84c499fe80c8416370117e5332fb5b4a2e18a541a51b44ce5995ceec05fdfcb629dfa2fc46abb477a443329724a656bdbc5ca77506915844ae5bef'),
        _hb.unhexlify('9792837144286d29b21edc6f8ce2b1cf4942a132ab9608daf9a32997a55eb7c4d8e3b1ed49ed797af3857be96a1220a4e5484e5974de63fd375fa0a0d8980165e5df66a8486aaee98ac6ea6c64cd75f1788f536f3ca147cfafdc6421a3eec6d602a31117a8ccde0950df720d929a3af2d93e0790fa15b0ba6b1276d2aec87ffe'),
        _hb.unhexlify('721fb0f3d1fb7614a811c4e3a4f868fa548b79baf446d8a66a25850fc0c712245e6a50f53c3dd989a403b4cfaf344ce046cdd5d8927c042f3b311b0164ad9a905e8fe375fad392749f0601e1a0d085c1d19c39c82fffd8a733e2d2454991296011d72e63d080cc9dbbc9cefe118de4cce7107b733fc8707f7fe3a5d40714789c'),
        _hb.unhexlify('ab158108ce933db9db55da6575bcc77a13ab58ca50b0727d378d523e9fa36fe1afc9b86550b7bf6cbf3e00675bdecccea8df70a75bb8bd2bd64d8abb912ce54955ba3db11e66917b1287353589fdef0283e3a8d2edf532fe64b2eb87eedfe6aa42c9e85c200219131758d67cbacf2f9483f139cd0fc1ad04701b24c8bc13e120'),
        _hb.unhexlify('aa727565c68bdfb77db36d69fce98a2159f9a7bcb64ace390686468ce517b0729c2410e8cf324115d3e7f62dde678745b5ca027781d3c2478ccaedbae1b9cf2360cc60210464fe39d4f9e11a6981c641ee35750751c769c271b26aac48670dcce0680ea4e5b292e2310df191c714562d5a2307f0dc89443b564e775b540191cb'),
        _hb.unhexlify('65b52a4787ecbf1758b31d6937f4312a12e0259b0a08151aba0bb1f9501748df78171c41fedb1f2c1ff815780e80b14ed353c0f66ff8e913a1809a69f0938375a4037f906ffa5f646c01e4053167490f54c522fe6e3269bd89e7eddb3e4c621f9ed6768f401a1d6730c0625a7bbbedd88e22ed030df0c7096ca7592b2c97df6a'),
        _hb.unhexlify('72e0d4a2a152e929180a7bf15ba39d0cb9dad5543b8a1d63503d627691823480d9ceddc8076ee99e1e3a239df86ad28fef0a0a4dc64d80075ab664c943b3a02c37f1a7b176cdbe8934ff151d074e6808c35074b604d3d04c4dc7edb0615c48c663a5e6a0044468f33eaffb9542e864814380fb8361b7f9f5ad57e38e37bb96a1'),
    )
    _inv = (14, 5, 12, 9, 13, 0, 2, 8, 3, 6, 10, 11, 16, 7, 4, 15, 1)
    _leaves = (
        _hb.unhexlify('c8f254f28008e53adc78cae4d44505dc53e2b8b8c818cec8194d7e4b0564f57a'),
        _hb.unhexlify('b62e94679a881530995bf02efb4ddc921d1120602e504d3d8ce7190502d52dc8'),
        _hb.unhexlify('9bdd8257a76b1d1e90293faffd023e4d3b2b91afdbb00c61d27571c9be19b8f0'),
        _hb.unhexlify('e0d6aa374833345911d54ec915afd2feb5fdb212085ff262d87b522680120cab'),
        _hb.unhexlify('5f640fa48ccb2a992e78a3bbb0c592739925ba414bf8eaaccc2ce96eadb2a7b1'),
        _hb.unhexlify('c85d6f8c231a492a3f548e27bcee30a9fd03add34f43e852488d2bbad3feccb0'),
        _hb.unhexlify('31f9c3618a05891218ab46163177c76fe6e6f8871704ba4f0f672a5d0258b4de'),
        _hb.unhexlify('3ccdd3b8bc8bb7fcd683ae368d62cefe074b9e75ceb9476c3137a91bf821b75f'),
        _hb.unhexlify('4e5ea54de748e5232e003340e02c3d182c5f909cfe0b03f981a0c1bcc97adf4a'),
        _hb.unhexlify('531b1717d10709f3968207a3d4c916f37336ee3ee8a146df40514ff00eaaf161'),
        _hb.unhexlify('90fffac6f0a56117e4e469567d6f43b0602b0a9c537a724e58d529c7105ed3c9'),
        _hb.unhexlify('24a477e2bd48cd5ede0afc1965e23e650ee2d732292273449479a31964d63e2c'),
        _hb.unhexlify('6e7db470352a8bc0a9fd509e833ef0324a7e77f2f8d5b27cbebcd53038862046'),
        _hb.unhexlify('1eb9a0e717a836a739e83f05433aadfb703b74d1dce060af9023de8acde15985'),
        _hb.unhexlify('18f8f63772195a39cfbc39504f2d41eb471b4c21e68509465349e9cfafca0bf3'),
        _hb.unhexlify('ed365e94ea3923b3180fda739f50733796c877b29be2a7fc7d5f77777a5b3f55'),
        _hb.unhexlify('3ce74181a0e7a67e1d73c92e180abbedff8b9e061ff74bf4a4a4a06dd1946125'),
    )
    _root = _hb.unhexlify('25ed749e7599fdf8b434510dad43a53998514017068d4d55db424e7357c7d2f4')
    _share1 = _hb.unhexlify('55eda5f163d89abc0fa9ee2f50360fb8a1798cbdee89b7724aa601d666ef165c')
    _share2 = _hb.unhexlify('9f79c9c5af812421529d38fa0edc11dc26853438e917cd18eb1ba098b56c4e3b')

    def _u32(_n):
        return _hs.pack('>I', _n)


    def _xor(_a, _c):
        _o = bytearray(len(_a))
        _i = 0
        while _i < len(_a):
            _o[_i] = _a[_i] ^ _c[_i]
            _i += 1
        return bytes(_o)

    def _ks(_key, _index, _length):
        _o = bytearray()
        _counter = 0
        _seed = _key + _u32(_index)
        while len(_o) < _length:
            _o.extend(_hh.sha256(_seed + _u32(_counter)).digest())
            _counter += 1
        return bytes(_o[:_length])

    def _merkle(_values):
        if not _values:
            return _hh.sha256(b'').digest()
        _level = list(_values)
        while len(_level) > 1:
            if len(_level) & 1:
                _level.append(_level[-1])
            _next = []
            _i = 0
            while _i < len(_level):
                _next.append(_hh.sha256(_level[_i] + _level[_i + 1]).digest())
                _i += 2
            _level = _next
        return _level[0]

    _key = _xor(_share1, _share2)
    _parts = []
    _verify = []
    _i = 0
    while _i < len(_inv):
        _masked = _b[_inv[_i]]
        _raw = _xor(_masked, _ks(_key, _i, len(_masked)))
        _parts.append(_raw)
        _verify.append(_hh.sha256(_u32(_i) + _raw).digest())
        _i += 1

    if tuple(_verify) != _leaves or _merkle(_verify) != _root:
        raise ImportError('HKD protected payload integrity verification failed')

    try:
        _source = _hz.decompress(b''.join(_parts)).decode('utf-8')
    except Exception as _exc:
        raise ImportError('HKD protected payload reconstruction failed: %s' % (_exc,))

    _filename = _g.get('__file__') or '<HKD-obfuscated>'
    _code = compile(_source, _filename, 'exec', 0, True, 0)

    # Discard the plaintext string before running user code.  CPython may reclaim
    # it immediately; no plaintext source is retained as a module global.
    del _source

    # Return the compiled payload.  Keep exec out of this function: older
    # CPython parsers reject an exec statement in a function that also contains
    # nested functions/free variables.  Execution happens at module scope below.
    return _code

_hkd_v4_code = _hkd_v4_bootstrap(globals())
del _hkd_v4_bootstrap

# Exact module semantics: execute in the real module globals.
exec(_hkd_v4_code, globals(), globals())
del _hkd_v4_code
