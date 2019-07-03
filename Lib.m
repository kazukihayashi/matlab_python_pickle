classdef Lib
    properties
        name
        scalar
        vector
        matrix
    end
    methods
        function obj = Lib()
            obj.name = 'Matlab';
            obj.scalar = 50.0;
            obj.vector = [5.0,5.0,5.0,5.0,5.0];
            obj.matrix = [1.1e3,1.2,1.3; 2.1,2.2,2.3];
        end
        function save(obj)
            file = py.open('data.p','wb');
            keys = ['first','second'];
            
            for j = 1:2
                a.keys(j) = struct(obj);
                props = properties(obj);
                for i = 1:length(props)
                    if isa(a.keys(j).(props{i}),'string') || isa(a.keys(j).(props{i}),'char')
                        continue
                    else
                        a.keys(j).(props{i}) = mat2str(a.keys(j).(props{i}));
                    end
                end
            end
            
            b = a.keys(1);
            %py.pickle.dump(a,file); %error if struct of structs
            py.pickle.dump(b,file);
            file.close();
        end
        function obj = load(obj)
            file = py.open('data.p','rb');
            all_dic = py.pickle.load(file);
            file.close();
            
            dic = all_dic{'first'};
            props = properties('obj');
            for i = 1:length(props)
                try
                    obj.(props{i}) = eval(string(dic{props{i}}));
                catch error
                    if strcmp(error.identifier,'MATLAB:dispatcher:InexactCaseMatch') || strcmp(error.identifier,'MATLAB:UndefinedFunction')
                        obj.(props{i}) = string(dic{props{i}});
                    else
                        rethrow(error)
                    end
                end
            end
        end
    end
end