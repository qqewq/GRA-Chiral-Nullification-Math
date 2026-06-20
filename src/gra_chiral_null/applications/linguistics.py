"""
Хиральность в языке: синтаксические зеркальные структуры.
Обнулёнка порождает грамматические оппозиции (актив/пассив).
"""
def sentence_as_chiral_pair(active_sentence: str, Z: callable) -> tuple:
    """Активный залог → пассивный как зеркальное отражение."""
    # Z переупорядочивает дерево зависимостей
    passive = Z(active_sentence)
    return (active_sentence, passive)

# Пример простого Z: меняет местами подлежащее и дополнение
def mirror_syntax(s: str):
    parts = s.split()
    if len(parts) >= 3:
        parts[0], parts[2] = parts[2], parts[0]
    return ' '.join(parts)

print(sentence_as_chiral_pair("cat eats mouse", mirror_syntax))
# ('cat eats mouse', 'mouse eats cat')
