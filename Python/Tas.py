class Tas:
    sah_cekiyor_mu = False

    def __init__(self, takim, pozisyon, resim):
        self.takim = takim
        self.pozisyon = pozisyon
        self.resim = resim


class Sah(Tas):
    tehlike = False

    def __init__(self, takim, pozisyon, resim):
        super().__init__(takim, pozisyon, resim)


class Piyon(Tas):
    sah_cekiyor_mu = False

    def __init__(self, takim, pozisyon, resim):
        super().__init__(takim, pozisyon, resim)


class Fil(Tas):
    sah_cekiyor_mu = False

    def __init__(self, takim, pozisyon, resim):
        super().__init__(takim, pozisyon, resim)


class At(Tas):
    sah_cekiyor_mu = False

    def __init__(self, takim, pozisyon, resim):
        super().__init__(takim, pozisyon, resim)


class Kale(Tas):
    sah_cekiyor_mu = False

    def __init__(self, takim, pozisyon, resim):
        super().__init__(takim, pozisyon, resim)


class Vezir(Tas):
    sah_cekiyor_mu = False

    def __init__(self, takim, pozisyon, resim):
        super().__init__(takim, pozisyon, resim)
