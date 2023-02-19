venvで環境管理を行う

インストールは以下のように行う

```bash
https://packaging.python.org/ja/latest/guides/installing-using-pip-and-virtual-environments/
```

パッケージ管理を行いたいディレクトリにて以下を実行し、構成ファイルを生成する。

```bash
python3 -m venv env
```

活性化する
```bash
source env/bin/activate
```

非活性は以下   
```bash
deactivate
```

依存関係は以下で生成・更新される。

```pip freeze > requirements.txt
pip install -r requirements.txt
pip uninstall -r requirements.txt -y
```

パッケージを削除した場合は以下でrequirements.txtを更新する

```
pip install pip-autoremove
pip-autoremove python-dateutil -y```

参考  
https://learn.microsoft.com/ja-jp/training/modules/python-create-manage-projects/5-exercise-manage-project-file