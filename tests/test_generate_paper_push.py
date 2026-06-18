import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "generate_paper_push", ROOT / "scripts" / "generate_paper_push.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

VALIDATOR_SPEC = importlib.util.spec_from_file_location(
    "validate_paper_push_dois", ROOT / "scripts" / "validate_paper_push_dois.py"
)
VALIDATOR = importlib.util.module_from_spec(VALIDATOR_SPEC)
sys.modules[VALIDATOR_SPEC.name] = VALIDATOR
VALIDATOR_SPEC.loader.exec_module(VALIDATOR)


class TranslationTests(unittest.TestCase):
    def test_translation_chunks_keep_short_sentences(self):
        text = "Short sentence. This is a longer sentence that must also be retained."
        self.assertEqual(" ".join(MODULE.translation_chunks(text)), text)

    def test_partial_translation_is_retried_by_sentence(self):
        source = (
            "This first English sentence is deliberately long enough to trigger residue detection. "
            "This second English sentence is also deliberately long enough for the same check."
        )
        responses = [
            [[[source, source]]],
            [[["这是第一句完整的中文翻译。", source]]],
            [[["这是第二句完整的中文翻译。", source]]],
        ]
        with patch.object(MODULE, "http_json", side_effect=responses), patch.object(
            MODULE.time, "sleep"
        ):
            translated = MODULE.translate_to_chinese(source)
        self.assertEqual(translated, "这是第一句完整的中文翻译。 这是第二句完整的中文翻译。")
        self.assertFalse(MODULE.has_excessive_english(translated))

    def test_excessive_english_is_detected(self):
        mixed = (
            "摘要：这是一小段中文。 This paragraph remains substantially in English and "
            "contains enough untranslated words to represent the production regression."
        )
        self.assertTrue(MODULE.has_excessive_english(mixed))
        self.assertTrue(VALIDATOR.has_excessive_english(mixed))


if __name__ == "__main__":
    unittest.main()
