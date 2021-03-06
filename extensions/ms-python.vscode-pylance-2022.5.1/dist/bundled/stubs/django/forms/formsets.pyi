from typing import Any, Dict, Generic, Iterator, List, Mapping, Optional, Sequence, Sized, Type, TypeVar, Union

from django.forms.forms import BaseForm, Form
from django.forms.utils import ErrorList, _DataT, _FilesT
from django.forms.widgets import Media, Widget
from django.utils.safestring import SafeString

TOTAL_FORM_COUNT: str = ...
INITIAL_FORM_COUNT: str = ...
MIN_NUM_FORM_COUNT: str = ...
MAX_NUM_FORM_COUNT: str = ...
ORDERING_FIELD_NAME: str = ...
DELETION_FIELD_NAME: str = ...

DEFAULT_MIN_NUM: int = ...
DEFAULT_MAX_NUM: int = ...

_F = TypeVar("_F", bound=BaseForm)

class ManagementForm(Form):
    cleaned_data: Dict[str, Optional[int]]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def clean(self) -> Dict[str, Optional[int]]: ...

class BaseFormSet(Generic[_F], Sized):
    form: Type[_F]
    extra: int
    can_order: bool
    can_delete: bool
    can_delete_extra: bool
    min_num: int
    max_num: int
    absolute_max: int
    validate_min: bool
    validate_max: bool

    is_bound: bool = ...
    prefix: Optional[str] = ...
    auto_id: str = ...
    data: _DataT = ...
    files: _FilesT = ...
    initial: Optional[Sequence[Mapping[str, Any]]] = ...
    form_kwargs: Dict[str, Any] = ...
    error_class: Type[ErrorList] = ...
    ordering_widget: Type[Widget]
    def __init__(
        self,
        data: Optional[_DataT] = ...,
        files: Optional[_FilesT] = ...,
        auto_id: str = ...,
        prefix: Optional[str] = ...,
        initial: Optional[Sequence[Mapping[str, Any]]] = ...,
        error_class: Type[ErrorList] = ...,
        form_kwargs: Optional[Dict[str, Any]] = ...,
        error_messages: Optional[Mapping[str, str]] = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[_F]: ...
    def __getitem__(self, index: int) -> _F: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    @property
    def management_form(self) -> ManagementForm: ...
    def total_form_count(self) -> int: ...
    def initial_form_count(self) -> int: ...
    @property
    def forms(self) -> List[_F]: ...
    def get_form_kwargs(self, index: Optional[int]) -> Dict[str, Any]: ...
    @property
    def initial_forms(self) -> List[_F]: ...
    @property
    def extra_forms(self) -> List[_F]: ...
    @property
    def empty_form(self) -> _F: ...
    @property
    def cleaned_data(self) -> List[Dict[str, Any]]: ...
    @property
    def deleted_forms(self) -> List[_F]: ...
    @property
    def ordered_forms(self) -> List[_F]: ...
    @classmethod
    def get_default_prefix(cls) -> str: ...
    @classmethod
    def get_ordering_widget(cls) -> Type[Widget]: ...
    def non_form_errors(self) -> ErrorList: ...
    @property
    def errors(self) -> List[ErrorList]: ...
    def total_error_count(self) -> int: ...
    def is_valid(self) -> bool: ...
    def full_clean(self) -> None: ...
    def clean(self) -> None: ...
    def has_changed(self) -> bool: ...
    def add_fields(self, form: _F, index: Optional[int]) -> None: ...
    def add_prefix(self, index: Union[int, str]) -> str: ...
    def is_multipart(self) -> bool: ...
    @property
    def media(self) -> Media: ...
    def as_table(self) -> SafeString: ...
    def as_p(self) -> SafeString: ...
    def as_ul(self) -> SafeString: ...

def formset_factory(
    form: Type[_F],
    formset: Type[BaseFormSet[_F]] = ...,
    extra: int = ...,
    can_order: bool = ...,
    can_delete: bool = ...,
    max_num: Optional[int] = ...,
    validate_max: bool = ...,
    min_num: Optional[int] = ...,
    validate_min: bool = ...,
    absolute_max: Optional[int] = ...,
    can_delete_extra: bool = ...,
) -> Type[BaseFormSet[_F]]: ...
def all_valid(formsets: Sequence[BaseFormSet[_F]]) -> bool: ...
