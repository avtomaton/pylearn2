""" Include tests related to Theano.

1) One test on one thing Pylearn2 depend to be done by Theano.
2) One test for a rare corner case crash in Theano that we where not
able to reproduce rapidly enough without having this tests depend on
Pylearn2.

"""

__authors__ = "Ian Goodfellow"
__copyright__ = "Copyright 2010-2012, Universite de Montreal"
__credits__ = ["Ian Goodfellow"]
__license__ = "3-clause BSD"
__maintainer__ = "LISA Lab"
__email__ = "pylearn-dev@googlegroups"
from theano import tensor as T


def test_grad():
    """Tests that the theano grad method returns a list if it is passed a list
        and a single variable if it is passed a single variable.
       pylearn2 depends on theano behaving this way but theano developers have
       repeatedly changed it """

    X = T.matrix()
    y = X.sum()

    G = T.grad(y, [X])

    assert isinstance(G, list)

    G = T.grad(y, X)

    assert not isinstance(G, list)
