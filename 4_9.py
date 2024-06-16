def all_variants(stroka):
    for nachalo in range(len(stroka)):
        for konec in range(nachalo + 1, len(stroka) + 1):
            yield stroka[nachalo:konec]


a = all_variants("abc")
for i in a:
    print(i)