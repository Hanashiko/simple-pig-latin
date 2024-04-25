def pig_it(text: str) -> None:
    plited_text: list[str] = text.split()
    result_list: list[str] = []
    for i in plited_text:
        result_list.append(f"{i[1:]}{i[0]}ay") if (i != "!" and i != "?" and i != ".") else result_list.append(i)
    return " ".join(result_list)

print(pig_it("Pig latin is cool ?"))
