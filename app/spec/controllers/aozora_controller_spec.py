import json

from mamba import description, context, it
from expects import expect, be_true, equal

from service.aozora_service import AozoraService

with description('aozora_controller') as self:
    with context('xxxに成功する場合'):
        with it('jsonを返却する'):
            expected_value = json.dumps({"key": 'value'})
            expect(AozoraService.search()).to(equal(expected_value))
