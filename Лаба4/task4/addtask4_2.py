import ruamel.yaml
import json
import timeit
time2 = 0
for k in range(100):
    yaml = ruamel.yaml.YAML(typ='safe')
    with open('C:\study\labs\инфа\Лаба4\Вторник.yml', encoding="utf-8") as f_in:
        data = yaml.load(f_in)
    with open('C:\study\labs\инфа\Лаба4\Вторник(итог)(для тестов).json', 'w', encoding="utf-8") as f_out:
        json.dump(data, f_out, indent=2, ensure_ascii=False)
        time2 += timeit.timeit()
print(str(time2) + ' - addtask 1')
