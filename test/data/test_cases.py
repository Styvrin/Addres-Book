
import pytest
from test.data.models import AddressBookData


ADD_GROUP_PARAMETRIZE = [
    pytest.param(
        AddressBookData(
            group='Group1',
            horr='Horr1',
            comment='comment1',
        ),
        id='All parametrize'
    ),
    pytest.param(
        AddressBookData(
            group='Group2',
            horr='',
            comment='comments2',
        ),
        id='Partly parametrize'
    ),
    pytest.param(
        AddressBookData(
            group='',
            horr='',
            comment='',
        ),
          # Все поля пустые
        id='Empty parametrize'
    )
]


EDIT_GROUP_PARAMETRIZE = [
pytest.param(
        AddressBookData(
            group='Edit group',
            horr='Edit eorr',
            comment='Edit comment1',
        ),
        id='Edit parametrize'
    )
]


ADD_USERS_PARAMETRIZE = [
    pytest.param(
        AddressBookData(
            first_name='Ivan',
            middle_name='Vladimirovich',
            last_name='Alibov',
            nickname='IvanVP',
            title='Senior accountant',
            company='MVPS Inc',
            address='221b, Baker Street, London, NW1 6XE, UK',
            home='+321 (985) 555-78',
            mobile='+7644 (657) 343-3223',
            work='+854 (115) 3453-3223',
            email1='sadfask@gmail.cums',
            email2='jkgasd2313udf@bk.com',
            email3='asdllmkgfgs@gdfg.mex',
            homepage='https://www.addressbook.dev',
            day_birtday='23',
            month_birtday='May',
            age__birtday='1985',
            day_anniversary='1',
            month_anniversary='October',
            age_anniversary='2006'
        ),
        id='All parametrize'
    ),
    pytest.param(
        AddressBookData(
            first_name='Peter',
            middle_name='Alexeyevich',
            last_name='Pupkin',
            nickname='PupkinPA',
            title='',
            company='',
            address='1234 Oak Street, Suite 200, San Francisco, CA 94105, USA',
            home='',
            mobile='+12134 (413245) 523455-1242334',
            work='',
            email1='Peter.Alexeyevich@sdfsf.com',
            email2='',
            email3='',
            homepage='',
            day_birtday='22',
            month_birtday='February',
            age__birtday='2003',
            day_anniversary='6',
            month_anniversary='July',
            age_anniversary='2021'
        ),
        id='Partly parametrize'
    ),
    pytest.param(
        AddressBookData(
        first_name='',
        middle_name='',
        last_name='',
        nickname='',
        title='',
        company='',
        address='',
        home='',
        mobile='',
        work='',
        email1='',
        email2='',
        email3='',
        homepage='',
        day_birtday='',
        month_birtday='',
        age__birtday='',
        day_anniversary='',
        month_anniversary='',
        age_anniversary=''
        ),
          # Все поля пустые
        id='Empty parametrize'
    )
]



EDIT_USERS_PARAMETRIZE = [
    pytest.param(
        AddressBookData(
        first_name='Emma',
        middle_name='Louise',
        last_name='Williams',
        nickname='Em',
        title='Marketing Director',
        company='Creative Minds Ltd',
        address='45 Baker Street, London, W1U 8EW, UK',
        home='+44 20 7946 0958',
        mobile='+44 7700 900123',
        work='+44 20 7946 0999',
        email1='emma.williams@creativeminds.co.sq',
        email2='emma.louise@gmasl.com',
        email3='emw@outlook.csa',
        homepage='https://www.emmawilliams.co.daf',
        day_birtday='23',
        month_birtday='March',
        age__birtday='1990',
        day_anniversary='12',
        month_anniversary='february',
        age_anniversary='2015'
        ),
        id='Edit parametrize'
    ),
]