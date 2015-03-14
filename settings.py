#!/usr/bin/python

import os
import yaml

general = yaml.load(open(os.path.expanduser("~/agents_settings/general.yaml")).read())
del os
del yaml
