# Compare this file to:
# https://github.com/open-contracting/standard_profile_template/blob/master/schema/apply-extensions.py

import os
import sys

from ocds_documentation_support import apply_extensions

basedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(basedir, '..', 'docs'))

from conf import extension_registry_git_ref  # noqa

apply_extensions(basedir, extension_registry_git_ref, 'gpa', [
    'ocds_recurrence_extension',
    'ocds_options_extension',
    'ocds_procurementMethodModalities_extension',
    'ocds_coveredBy_extension',
    # 'ocds_party_classifications_extension',
    # 'ocds_tender_mainItemClassification_extension',
    # 'ocds_tender_legalBasisDetails_extension',
])
