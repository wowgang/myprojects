#출력#출력
# print('a -', f['name']) # name n이 소문자는 존재 하지않는다 -> 에러가 발생한다
print('a -', f.get('name')) #nome 존재x => nome출력
print('b -', b[0]) #b - Hello Python
print('b -', b.get(0)) #b - Hello Python
print('f-', f['City'])
print('f-', f.get('Age'))

#딕셔너리 추가
a = {'name': 'superman', 'phon_num': '01046295415', 'birth' : '990119'}
a['address'] = ['940-1']
print('a -', a)
a['rank'] = [1,2,3]
print('a -', a)

#key 기준으로 문자길이 센다. (key ,vaule가 한쌍)
print('a-', len(a))
print('b-', len(b))
print('c-', len(c))
print('d-', len(d))
print('e-', len(e))
print('f-', len(f))

a = {'name': 'superman', 'phon_num': '01046295415', 'birth' : '990119'}
print('a -', a.pop('name')) #리스트나 듀플에서pop맨끝자리를 뽑아냈으나 딕셔너리에서는 해당되는 key의 value 값이 출력됨
#순서가 없어서 key를 기준으로 끄집어냄
print(a) # {'phon_num': '01046295415', 'birth': '990119'} 위에서 pop을 해서 빠졌음


c = {'arr' : [1,2,3,4,5]}
print('c -', c.pop('arr')) #c - [1, 2, 3, 4, 5]
print(c) #{}

f = dict(
    Name = 'Niceman' ,
    City = 'Suwon' ,
    Age = 25 ,
    Grade = 'A' ,
    Status = True
)

print('f -', f.popitem()) # 딕셔너리의 맨 마지막 자리 key 출력  f - ('Status', True)
print('f -', f) # f - {'Name': 'Niceman', 'City': 'Suwon', 'Age': 25, 'Grade': 'A'}
#popitem다섯번 사용하면 다빠짐 원래 우리가 사용하던 pop의용도

a = {'name': 'superman', 'phon_num': '01046295415', 'birth' : '990119'}
print('a -', 'birth' in a) #a - True
print('a -', 'City' in a) #a - False

a['test'] = 'test_dict'
print(a) # {'name': 'superman', 'phon_num': '01046295415', 'birth': '990119', 'tet': 'test_dict'}
a['test'] = 'test_dict_01'
print(a)  #{'name': 'superman', 'phon_num': '01046295415', 'birth': '990119', 'test': 'test_dict_01'} 중복안되기때문에 덮어씌움

a.update(birth = '0808')
print(a) #{'name': 'superman', 'phon_num': '01046295415', 'birth': '0808', 'test': 'test_dict_01'} birth수정됨

#keys 없으면 추가하고 keys가 있으면 수정한다.
