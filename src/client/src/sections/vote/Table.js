const table = [
  {
    id: 1,
    name: 'ביטחון',
    budget: '20',
    checked: false,
    children: [
      {
        id: 2,
        name: 'צה"ל',
        budget: '15',
        checked: false,
      },
      {
        id: 3,
        name: 'משרד הביטחון',
        budget: '5',
        checked: false,
      },
    ],
  },
  {
    id: 4,
    name: 'כלכלה',
    budget: '40',
    checked: false,
    children: [
      {
        id: 5,
        name: 'הייטק',
        budget: '20',
        checked: false,
      },
      {
        id: 6,
        name: 'בנק',
        budget: '10',
        checked: false,
      },
      {
        id: 7,
        name: 'פנסיה',
        budget: '10',
        checked: false,
        children: [
          {
            id: 8,
            name: 'מייק',
            budget: '10',
            checked: false,
          },
        ],
      },
    ],
  },
  {
    id: 9,
    name: 'פנים',
    budget: '10',
    checked: false,
    children: [
      {
        id: 10,
        name: 'הייטק',
        budget: '1',
        checked: false,
      },
      {
        id: 11,
        name: 'בנק',
        budget: '4',
        checked: false,
      },
      {
        id: 12,
        name: 'פנסיה',
        budget: '5',
        checked: false,
        children: [
          {
            id: 13,
            name: 'מייק',
            budget: '3',
            checked: false,
            children: [
              {
                id: 141,
                name: 'תרבות',
                budget: '1',
                checked: false,
                children: [
                  {
                    id: 151,
                    name: 'בריאות',
                    budget: '1',
                    checked: false,
                    children: [
                      {
                        id: 161,
                        name: 'תרבות',
                        budget: '1',
                        checked: false,
                      },
                    ],
                  },
                ],
              },
              {
                id: 142,
                name: 'ספורט',
                budget: '1',
                checked: false,
              },
              {
                id: 143,
                name: 'אוצר',
                budget: '1',
                checked: false,
              },
            ],
          },
          {
            id: 131,
            name: 'ימייק',
            budget: '1',
            checked: false,
          },
          {
            id: 132,
            name: 'חינוך',
            budget: '1',
            checked: false,
          },
        ],
      },
    ],
  },
  {
    id: 14,
    name: 'כלכלה',
    budget: '10',
    checked: false,
  },
  {
    id: 15,
    name: 'סביבה',
    budget: '5',
    checked: false,
  },
  {
    id: 16,
    name: 'פנים',
    budget: '5',
    checked: false,
  },
  {
    id: 17,
    name: 'ספורט',
    budget: '5',
    checked: false,
  },
  {
    id: 18,
    name: 'דתות',
    budget: '5',
    checked: false,
  },
];

export default table;
