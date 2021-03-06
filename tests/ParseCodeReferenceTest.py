# -*- coding: utf-8 -*-

from DuralexTestCase import DuralexTestCase

import duralex.alinea_parser as parser

class ParseCodeReferenceTest(DuralexTestCase):
    def test_code_with_name(self):
        self.assertEqualAST(
            self.call_parse_func(
                parser.parse_code_reference,
                "le code de l\'éducation"
            ),
            {'children':[
                {
                    'codeName': u'code de l\'éducation',
                    'type': u'code-reference'
                }
            ]}
        )

    def test_code_with_name_2(self):
        self.assertEqualAST(
            self.call_parse_func(
                parser.parse_code_reference,
                "du code de l\'éducation"
            ),
            {'children':[
                {
                    'codeName': u'code de l\'éducation',
                    'type': u'code-reference'
                }
            ]}
        )

    def test_the_same_code(self):
        self.assertEqualAST(
            self.call_parse_func(
                parser.parse_code_reference,
                "le même code",
                {'children':[
                    {
                        'codeName': u'code de l\'éducation',
                        'type': u'code-reference'
                    }
                ]}
            ),
            {'children':[
                {
                    'codeName': u'code de l\'éducation',
                    'type': u'code-reference'
                },
                {
                    'codeName': u'code de l\'éducation',
                    'type': u'code-reference'
                }
            ]}
        )

    def test_the_same_code_2(self):
        self.assertEqualAST(
            self.call_parse_func(
                parser.parse_code_reference,
                "du même code",
                {'children':[
                    {
                        'codeName': u'code de l\'éducation',
                        'type': u'code-reference'
                    }
                ]}
            ),
            {'children':[
                {
                    'codeName': u'code de l\'éducation',
                    'type': u'code-reference'
                },
                {
                    'codeName': u'code de l\'éducation',
                    'type': u'code-reference'
                }
            ]}
        )
