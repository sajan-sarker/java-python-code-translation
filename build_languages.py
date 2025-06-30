# build_languages.py
from tree_sitter import Language

Language.build_library(
  'evaluator/CodeBLEU/parser/my-languages.so',  # Adjust this path if needed
  [
    'tree-sitter-java',
    'tree-sitter-python'
  ]
)
