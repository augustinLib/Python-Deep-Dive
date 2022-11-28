def clip(text:str, max_len:'int > 0' = 80) -> str:
    """
    max_len 앞이나 뒤의 마지막 공백에서 잘라낸 텍스트 반환
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(" ", 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(" ", max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].rstrip()

