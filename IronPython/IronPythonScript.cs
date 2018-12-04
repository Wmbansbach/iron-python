using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RABTAXES_SOURCE
{
    class IronPythonScript
    {
    /*
    * Awesome Way to embed python scripts with iron python
    * ensure that python modules are not C based (matplot, pandas)
    * IronPython still does not support these modules at runtime
    * 
    public dManager(string date, string amount, string gas, dictUtil tools)
    {
        // Object array created to pass parameters to python script
        object[] param = new object[] {date, amount, gas, tools.expenses};
        // Creating IronPython interpreter
        ScriptEngine p_engine = Python.CreateEngine();
        // Defining script path
        string pythonPath = @"C:\Users\remov\Desktop\C#\dataManager.py";

        // Directing engine to correct python library search paths
        ICollection<string> paths = p_engine.GetSearchPaths();
        string dir = @"C:\Python35\Lib";
        paths.Add(dir);
        string _dir = @"C:\Python35\Lib\site-packages";
        paths.Add(_dir);
        p_engine.SetSearchPaths(paths);

        // Create source and scope for Python script
        ScriptSource p_source = p_engine.CreateScriptSourceFromFile(pythonPath);
        ScriptScope p_scope = p_engine.CreateScope();
        // Executing source code in scope
        p_source.Execute(p_scope);

        // class object instantiation from Python script "class"
        Object testClass = p_engine.Operations.Invoke(p_scope.GetVariable("dManager"));

        // call the instantiated member giving the method to be called and its parameters
        var result = p_engine.Operations.InvokeMember(testClass, "manage", param);
        MessageBox.Show("Program has completed!");
        // Exiting Application
        Application.Exit();
    }
    */
    }
}
