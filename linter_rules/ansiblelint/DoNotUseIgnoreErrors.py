from ansiblelint import AnsibleLintRule


class DoNotUseIgnoreErrors(AnsibleLintRule):
    id = 'RULE10'
    shortdesc = 'Do not use the ignore_errors parameter in the finished role'
    description = (
        'The ignore_errors setting swallows all errors, even ones you may not be expecting,'
        'and you risk leaving your host in a broken or unstable state'
    )
    severity = 'MEDIUM'
    tags = ['DoNotUseIgnoreErrors']

    def matchtask(self, file, task):
        return task.get('ignore_errors')
