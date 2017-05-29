from __future__ import division, print_function
import numpy as np
import scattering
import smatrix
import tmatrix
import matplotlib.pyplot as plt


def linear(se, chli, chlo, Es):
    """
    Linear component of the single particle transmittance.

    Parameters
    ----------
    se : scattering.Setup object
        Scattering setup object.
    chli : int
        Incoming channel.
    chlo : int
        Outgoing channel.
    Es : ndarray
        Single particle energies.
    """
    return np.abs(smatrix.one_particle(se, chli, chlo, Es)[1]) ** 2


def nonlinear(se, chli, chlo, Es, p=0.1):
    """
    Non-linear correction to the transmittance.

    Parameters
    ----------
    se : scattering.Setup object
        Scattering setup object.
    chli : int
        Incoming channel index.
    chlo : int
        Outgoing channel index.
    Es : ndarray
        Single particle energies.
    p : float
        The power = alpha**2/L (number of photons per time/pulse length)
    """
    tr = np.zeros((len(Es),), dtype=np.complex128)
    t2 = np.zeros((len(Es),), dtype=np.complex128)
    for chl in xrange(len(se.channels)):
        #  single particle contribution
        s1ij = smatrix.one_particle(se, chli, chl, Es)[1]

        # The t2 contribution
        for i, E in enumerate(Es):
            t2[i] = tmatrix.two_particle(se, (chli, chli), (chlo, chl), E=2 * E, dE=0, qs=np.array([E]))[1][0, 0]

        # result
        tr += 8 * 1j * (np.pi ** 2) * p * np.conjugate(s1ij) * t2

    s1 = smatrix.one_particle(se, chli, chlo, Es)[1]

    return np.abs(s1 - tr) ** 2, s1, tr


if __name__ == '__main__':

    def setitup(offset=0):

        d = 4

        omegas = [offset] * 2
        omegas[0] += d
        omegas[1] += -d

        m = scattering.Model(
            omegas=omegas,
            links=[[0, 1, 1]],
            U=[1] * 2)

        chnls = []
        chnls.append(scattering.Channel(0, .001 + 1 / np.sqrt(np.pi)))
        chnls.append(scattering.Channel(1, .001 + 1 / np.sqrt(np.pi)))

        se = scattering.Setup(m, chnls)

        return se

    ss1 = setitup(0)
    ss2 = setitup(-1)
    Es = np.linspace(-10, 10, 512)
    tt1 = nonlinear(ss1, 0, 1, Es)
    tt2 = nonlinear(ss2, 0, 1, Es)

    i = 0
    plt.plot(Es, np.real(tt1[i]))
    plt.plot(Es, np.imag(tt1[i]))
    plt.plot(Es + 1, np.real(tt2[i]))
    plt.plot(Es + 1, np.imag(tt2[i]))
    plt.show()
