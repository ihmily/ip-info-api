# API Test Workflow 使用说明

## 触发方式

### 1. 自动触发
- **定时任务**: 每3小时自动运行一次
- **PR/Push**: 推送到main分支时自动运行

### 2. 手动触发
在 GitHub Actions 页面点击 `workflow_dispatch` 按钮即可手动运行。

### 3. 通过commit消息触发
推送时如果commit消息**包含** `run action`（不区分大小写），会触发CI：
```bash
git commit -m "update api list run action" -m "some description"
```

推送时如果commit消息**包含** `[skip ci]`，则会跳过CI：
```bash
git commit -m "[skip ci] update readme"
```

## 输出说明

CI运行后会：
1. 执行 `python test_apis.py -c 32 -v --clear` 测试所有API
2. 更新 `README.md` 中的API状态表格
3. 生成测试结果JSON文件到 `output/` 目录

## 本地开发流程

```bash
# 1. 修改代码后，先commit本地改动
git add -A && git commit -m "your message"

# 2. 拉取远程最新代码并合并
git pull origin main --rebase

# 3. 推送到远程
git push origin main
```

> 注意：如果有未提交的改动又想拉取远程代码，使用 `git stash` 先暂存：
> ```bash
> git stash
> git pull origin main --rebase
> git stash pop
> ```

## 常见问题

### CI权限问题
如果CI报错 `Permission denied to github-actions[bot]`，需要：

1. 进入仓库 **Settings** → **Actions** → **General**
2. 在 **Workflow permissions** 中选择 **"Read and write permissions"**
3. 点击 **Save** 保存

或者不使用自动push，改用：
- 将结果发布到 GitHub Pages
- 或者只在本地运行后手动push
