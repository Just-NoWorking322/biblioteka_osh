from modeltranslation.translator import register, TranslationOptions
from app.about_library.models import AboutLibrary, TitlesLibrary, Management, Acts, History, StructureAndLibraries


@register(AboutLibrary)
class AboutLibraryTranslationOption(TranslationOptions):
    fields = ('title_1', 'title_2', 'description')

@register(TitlesLibrary)
class TitlesLibraryTranslationOption(TranslationOptions):
    fields = ('title_1', 'title_2', 'title_3', 'title_4')

@register(Management)
class ManagementTranslationOption(TranslationOptions):
    fields = ('role', 'full_name')

@register(Acts)
class ActsTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(History)
class HistoryTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(StructureAndLibraries)
class StructureAndLibrariesTranslationOption(TranslationOptions):
    fields = ('image',)