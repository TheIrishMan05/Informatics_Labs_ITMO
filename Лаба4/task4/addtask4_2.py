import ruamel.yaml
import json
import timeit
time2 = []
for k in range(100):
    yaml = ruamel.yaml.YAML(typ='safe')
    with open('C:\study\labs\инфа\Лаба4\Вторник.yml', encoding="utf-8") as f_in:
        data = yaml.load(f_in)
    with open('C:\study\labs\инфа\Лаба4\Вторник(итог)(для тестов).json', 'w', encoding="utf-8") as f_out:
        json.dump(data, f_out, indent=2)
        time2.append(timeit.timeit())
print(str((min(time2) + max(time2)) / 2) + ' - addtask 1')
