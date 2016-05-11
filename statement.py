from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['StatementLine']


class StatementLine:
    __name__ = 'account.bank.statement.line'
    __metaclass__ = PoolMeta

    user = fields.Many2One('res.user', 'User')
