按用户分配权限'''
用户表:
    id  name
    1   m5xhsy
权限表:
    id  user_id         url            title
    1      1        /App/index/       查看主页
    
'''
按角色分配权限(RBAC: role based access control)'''

用户表:
    id  name
    1   m5xhsy
角色表:
    id   title
    1     CEO
    2     销售
用户角色关系表:    多对多，一人可以多个角色，多个人可以同一个角色
    id    user_id     role_id
    1       1            2
角色权限关系表:
    id    role_id      permission_id
    1        1              1
权限表:
    id  user_id         url            title
    1      1        /App/index/       查看主页
'''





















