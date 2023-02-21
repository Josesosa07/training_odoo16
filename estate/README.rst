**Trainig odoo**

I have the src folder with the odoo repo and the enterpise repo, so I have src with: odoo, enterprise, then I created there a new folder called custom which has this repository.
I can run the code with from the virtual environment in the odoo repository.

```
./odoo-bin --addons-path=../custom,../enterprise/,addons -d rd-demo -u estate --dev xml
```
