from dataclasses import dataclass
import pandas as pd



@dataclass
class CrimeModel(object):
    _context : str = ''
    _dname : str = ''
    _sname : str = ''
    _fname : str = ''
    _crime : object = None
    _cctv : object = None
    _label : str = ''
    

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self,context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self,fname): self._fname = fname

    @property
    def dname(self) -> str: return self._dname

    @dname.setter
    def dname(self,dname): self._dname = dname

    @property
    def sname(self) -> str: return self._sname

    @sname.setter
    def sname(self,sname): self._sname = sname

    @property
    def crime(self) -> str: return self._crime

    @crime.setter
    def crime(self,_crime): self._crime = _crime

    @property
    def cctv(self) -> str: return self._cctv

    @cctv.setter
    def cctv(self,_cctv): self._cctv = _cctv


    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self,label): self._label = label


  