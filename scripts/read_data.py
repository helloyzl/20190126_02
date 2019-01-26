import pytest,yaml,os,sys
sys.path.append(os.getcwd())

def get_data():
    list1 = []
    with open('./data' + os.sep + 'data_test.yaml','r') as f:
        results = yaml.load(f)
        # print(results.get('data').values())
        contents = results.get('data').values()
        for i in contents:
            # print(i.values())
            list1.append(tuple(i.values()))
        print(list1)
        return list1

class Test_param:
    # @pytest.mark.parametrize('a,b,c',[(1,2,3),(4,5,9),(3,4,8)])
    @pytest.mark.parametrize('a,b,c',get_data())
    def test_judge_sum(self,a,b,c):
        assert a+b==c
