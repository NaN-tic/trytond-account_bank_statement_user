from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['StatementLine']
__metaclass__ = PoolMeta


class StatementLine:
    __name__ = 'account.bank.statement.line'
    user = fields.Many2One('res.user', 'User')
