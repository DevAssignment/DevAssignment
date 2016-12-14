import collections
import abc


class Enumerable(collections.Iterable, metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def __repr__(self):
    raise NotImplementedError('users must define __repr__ to use this base class')

  @abc.abstractmethod
  def move_next(self):
    raise NotImplementedError('users must define move_next to use this base class')

  @abc.abstractmethod
  def get_current(self):
    raise NotImplementedError('users must define get_current to use this base class')

  @abc.abstractmethod
  def get_at_index(self, index):
    raise NotImplementedError('users must define get_at_index to use this base class')

  @abc.abstractmethod
  def reset(self):
    raise NotImplementedError('users must define reset to use this base class')