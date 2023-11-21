hello world

# Issues to Resolve

- pydantic isn't being found by pyright right now ... not sure why.
- could be that pydantic isn't in the pyproject toml but it should still be picked up by the virtual env
- could be that pyright's finding it but vim isn't

after installing pydantic, prisma breaks. 
Okay so something weird happened with the venv file - deleting with rm -rf .venv fixed things
- this really points to how it's a great idea to have venv folders IN PROJECT so you don't have this mystical venv in some shared folder elsewhere.


## Pyright Issues

❯ pyright
/Users/nathanlaundry/Documents/projects/ACCESS-stack-spike/access_stack_spike/app.py
  /Users/nathanlaundry/Documents/projects/ACCESS-stack-spike/access_stack_spike/app.py:4:6 - error: Stub file not fo
und for "pydantic" (reportMissingTypeStubs)
  /Users/nathanlaundry/Documents/projects/ACCESS-stack-spike/access_stack_spike/app.py:4:22 - error: "BaseModel" is
unknown import symbol (reportGeneralTypeIssues)
  /Users/nathanlaundry/Documents/projects/ACCESS-stack-spike/access_stack_spike/app.py:4:22 - error: Type of "BaseMo
del" is unknown (reportUnknownVariableType)
  /Users/nathanlaundry/Documents/projects/ACCESS-stack-spike/access_stack_spike/app.py:12:19 - error: Base class typ
e is unknown, obscuring type of derived class (reportUntypedBaseClass)
  /Users/nathanlaundry/Documents/projects/ACCESS-stack-spike/access_stack_spike/app.py:3:21 - error: Import "Body" i
s not accessed (reportUnusedImport)
  /Users/nathanlaundry/Documents/projects/ACCESS-stack-spike/access_stack_spike/app.py:36:5 - error: Variable "bob"
is not accessed (reportUnusedVariable)
6 errors, 0 warnings, 0 informations
