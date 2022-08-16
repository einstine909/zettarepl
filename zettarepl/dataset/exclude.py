# -*- coding=utf-8 -*-
import logging
import fnmatch

import zettarepl.dataset.relationship

logger = logging.getLogger(__name__)

__all__ = ["should_exclude"]


def should_exclude(dataset: str, exclude: [str]):
    return any(zettarepl.dataset.relationship.is_child(dataset, excl) or fnmatch.fnmatch(dataset, excl) for excl in exclude)
