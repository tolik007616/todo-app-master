# TODO-app
Test task: simple todo lists for Ruby Garage

At first you need to login to be able to create projects. If you don't have an account you can create it by using a form at the top. Just type login and password and your account will be created automatically if there is no more users with same logins. Note that login is case sensitive.

The project have been deployed on [Heroku](https://herokuapp.com). You can try it [there](https://jason-to-do-app.herokuapp.com).

## Tests:

For running tests use 
```python
python manage.py test
```

## SQL Task:

### Given tables:

* Tasks (id, name, status, project_id)
* Projects (id, name)

### Technical requirements:

Get all statuses, not repeating, alphabetically ordered:
```sql
SELECT DISTINCT status FROM Tasks ORDER BY status
```

Get the count of all tasks in each project, order by tasks count descending:
```sql
SELECT t1.name as project_name, count(t2.id) as count_tasks FROM Projects as t1 LEFT JOIN Tasks as t2 ON t2.project_id = t1.id GROUP BY project_name ORDER BY count_tasks DESC
```

Get the count of all tasks in each project, order by project names:
```sql
Select count(t1.id),t2.name From Tasks as t1 JOIN Projects as t2 ON t2.id = t1.project_id GROUP BY project_id ORDER BY t2.name
```

Get the tasks for all projects having the name beginning with “N” letter:
```sql
SELECT t1.name as task, t2.name as project FROM Tasks as t1, Projects as t2 WHERE t2.name LIKE "N%" AND t1.project_id = t2.id
```

Get the list of all projects containing the “a” letter in the middle of the name, and show the tasks count near each project. Mention that there can exist projects without tasks and tasks with project_id=NULL:
```sql
SELECT t2.name as project, count(t1.id) as count_tasks FROM Projects as t2 LEFT JOIN Tasks as t1 on t1.project_id = t2.id WHERE t2.name LIKE "%a%" AND t2.name NOT LIKE "a%" AND t2.name NOT LIKE "%a" GROUP BY project
```

Get the list of tasks with duplicate names. Order alphabetically:
```sql
SELECT name FROM Tasks GROUP BY name HAVING count(*)>1 ORDER BY name
```

Get the list of tasks having several exact matches of both name and status, from the project Garage. Order by matches count:
```sql
SELECT t1.name, t1.status, COUNT(*) as task_count FROM Tasks as t1, Projects as t2 WHERE t2.name="Garage" AND t1.project_id = t2.id GROUP BY t1.name, t1.status HAVING count(*)>1 ORDER BY task_count
```

Get the list of project names having more than 10 tasks in status completed. Order by project_id:
```sql
SELECT t1.name FROM Projects as t1 Where t1.id IN (Select t2.project_id From Tasks as t2 Where t2.status = 0 HAVING count(*)>10) ORDER BY t1.id
```