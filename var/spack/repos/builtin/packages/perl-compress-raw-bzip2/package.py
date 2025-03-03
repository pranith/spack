# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCompressRawBzip2(PerlPackage):
    """A low-Level Interface to bzip2 compression library."""

    homepage = "https://metacpan.org/pod/Compress::Raw::Bzip2"
    url      = "http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/Compress-Raw-Bzip2-2.081.tar.gz"

    version('2.081', sha256='8692b5c9db91954408e24e805fbfda222879da80d89d9410791421e3e5bc3520')

    depends_on('bzip2')
    depends_on('perl-extutils-makemaker', type='build')
