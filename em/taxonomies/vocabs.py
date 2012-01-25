from zope.i18nmessageid import MessageFactory
_ = MessageFactory("plumi")

vocab_set = {}

taxonomy_sub_folder={'topic':'video_categories','genre':'video_genre','callouts':'submission_categories','countries':'video_countries'}

vocab_set['video_countries'] = (
         ('XX', _(' International')),
         ('BU', _('Bougainville')),
         ('TI', _('Tibet')),
         ('AQ', _('Antarctica')),
         ('HA', _('Hawaii')),
         ('WP', _('West Papua')),
         ('BN', _(u'Brunei Darussalam ')),
         ('MM', _(u'Myanmar ')),
         ('KH', _(u'Cambodia')),
         ('ID', _(u'Indonesia ')),
         ('LA', _(u'Lao People\'s Democratic Republic')),
         ('MY', _(u'Malaysia')),
         ('PH', _(u'Philippines ')),
         ('SG', _(u'Singapore ')),
         ('TH', _(u'Thailand')),
         ('VN', _(u'Viet Nam')),
         ('AQ', _(u'Antarctica')),
         ('AU', _(u'Australia ')),
         ('FJ', _(u'Fiji')),
         ('PF', _(u'French Polynesia')),
         ('GU', _(u'Guam')),
         ('HK', _(u'Hong Kong')),
         ('KI', _(u'Kiribati')),
         ('MH', _(u'Marshall Islands')),
         ('FM', _(u'Micronesia, Federated States Of ')),
         ('NZ', _(u'New Zealand ')),
         ('NR', _(u'Nauru ')),
         ('NC', _(u'New Caledonia ')),
         ('MP', _(u'Northern Mariana Islands')),
         ('PW', _(u'Palau ')),
         ('PG', _(u'Papua New Guinea')),
         ('PN', _(u'Pitcairn')),
         ('WS', _(u'Samoa ')),
         ('SB', _(u'Solomon Islands ')),
         ('TL', _(u'Timor-Leste')),
         ('TK', _(u'Tokelau ')),
         ('TO', _(u'Tonga ')),
         ('TV', _(u'Tuvalu')),
         ('VU', _(u'Vanuatu ')),
         ('CN', _(u'China ')),
         ('JP', _(u'Japan ')),
         ('KP', _(u'Korea, Democratic People\'s Republic Of')),
         ('KR', _(u'Korea, Republic Of')),
         ('MN', _(u'Mongolia')),
         ('TW', _(u'Taiwan')),
         ('BD', _(u'Bangladesh')),
         ('BT', _(u'Bhutan')),
         ('IN', _(u'India ')),
         ('MV', _(u'Maldives')),
         ('NP', _(u'Nepal ')),
         ('PK', _(u'Pakistan')),
         ('LK', _(u'Sri Lanka ')),
        )

vocab_set['video_categories'] = (
         ('poverty', _(u'Poverty / Development')),
         ('indigenous', _(u'Indigenous')),
         ('refugee', _(u'Refugee / Migration')),
         ('health', _(u'Health')),
         ('corporations', _(u'Corporations / Privatisation')),
         ('globalisation', _(u'Globalisation')),
         ('law', _(u'Law / Justice')),
         ('work', _(u'Work')),
         ('consumerism', _(u'Consumerism')),
         ('war', _(u'War / Peace')),
         ('human', _(u'Human Rights')),
         ('disability', _(u'Disability Rights')),
         ('gender', _(u'Gender / Sexuality')),
         ('race', _(u'Race')),
         ('religion', _(u'Religion')),
         ('art', _(u'Art / Culture')),
         ('internet', _(u'Internet')),
         ('media', _(u'Media')),
         ('activism', _(u'Activism')),
         ('politics', _(u'Politics')),
         ('education', _(u'Education')),
         ('biodiversity', _(u'Biodiversity')),
         ('climate', _(u'Climate Change')),
         ('conservation', _(u'Forests / Conservation')),
         ('nuclear', _(u'Nuclear')),
         ('sustainablity', _(u'Sustainability')),
         ('animal', _(u'Animal Rights')),
         ('water', _(u'Water')),
         ('biotech', _(u'Biotech')),
         ('civillib',_(u'Civil Liberties')),
        )
vocab_set['video_genre'] = (
         ('none', _(u'-- None --')),
         ('documentary', _(u'Documentary')),
         ('experimental', _(u'Experimental')),
         ('fiction', _(u'Fiction')),
         ('animation', _(u'Animation')),
         ('music', _(u'Music')),
         ('newsreport', _(u'News Report')),
        )
vocab_set['submission_categories'] = (
         ('none', _(u'----------------')),
         ('festival', _(u'Festival')),
         ('screening', _(u'Screening')),
         ('dvd', _(u'DVD')),
         ('production', _(u'Production')),
         ('conference', _(u'Conference')),
         ('workshop', _(u'Workshop')),
         ('crew', _(u'Crew')),
         ('competition', _(u'Competition')),
         ('artprize', _(u'Art Prize')),
         ('exhibition',_(u'Exhibition')),
         ('other', _(u'Other')),
        ) 

vocab_set['video_languages'] = (
        ('my', _(u'Burmese ')),
        ('km', _(u'Cambodian ')),
        ('ce', _(u'Cebuano ')),
        ('ind', _(u'Indonesian ')),
        ('jw', _(u'Javanese ')),
        ('ka', _(u'Karen ')),
        ('kh', _(u'Khmer ')),
        ('la', _(u'Lao ')),
        ('ma', _(u'Madurese ')),
        ('mg', _(u'Malagasy ')),
        ('ms', _(u'Malay ')),
        ('su', _(u'Sundanese ')),
        ('tl', _(u'Tagalog ')),
        ('te', _(u'Tetum ')),
        ('th', _(u'Thai ')),
        ('vi', _(u'Vietnamese ')),
        ('fi', _(u'Fijian ')),
        ('mi', _(u'Maori ')),
        ('sm', _(u'Samoan ')),
        ('to', _(u'Tongan ')),
        ('be', _(u'Bengali ')),
        ('hi', _(u'Hindi ')),
        ('ne', _(u'Nepali ')),
        ('pa', _(u'Punjabi ')),
        ('ta', _(u'Tamil ')),
        ('bo', _(u'Tibetan ')),
        ('si', _(u'Sinhala ')),
        ('ur', _(u'Urdu ')),
        ('ca', _(u'Cantonese ')),
        ('ja', _(u'Japanese ')),
        ('ko', _(u'Korean ')),
        ('man', _(u'Mandarin ')),
        ('mo', _(u'Mongolian ')),
        ('tai', _(u'Taiwanese ')),
        ('ar', _(u'Arabic ')),
        ('en', _(u'English ')),
        ('fr', _(u'French ')),
        ('de', _(u'German ')),
        ('it', _(u'Italian ')),
        ('pt', _(u'Portugese ')),
        ('ru', _(u'Russian ')),
        ('es', _(u'Spanish ')),
)
