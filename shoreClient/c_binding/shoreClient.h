int shorePut(char const *, char const *, const unsigned int, const unsigned int, const unsigned int *, const int, const void *);
int shoreQuery(char const *, char const *, unsigned int*, unsigned int *, int *);
int shoreGet(char const *, char const *, const unsigned int, const unsigned int, void *);
void shoreClientCyInit();

enum shoreDataType {
    shoreTypeBool = 0,
    shoreTypeChar = 1,
    shoreTypeUChar = 2,
    shoreTypeShort = 3,
    shoreTypeUShort = 4,
    shoreTypeInt = 5,
    shoreTypeUInt = 6,
    shoreTypeFloat= 7,
    shoreTypeDouble = 8,
    shoreTypeComplex = 9,
    shoreTypeDComplex = 10,
    shoreTypeString = 11,
    shoreTypeTable,
    shoreTypeArrayBool,
    shoreTypeArrayChar,
    shoreTypeArrayUChar,
    shoreTypeArrayShort,
    shoreTypeArrayUShort,
    shoreTypeArrayInt,
    shoreTypeArrayUInt,
    shoreTypeArrayFloat,
    shoreTypeArrayDouble,
    shoreTypeArrayComplex,
    shoreTypeArrayDComplex,
    shoreTypeArrayString,
    shoreTypeRecord,
    shoreTypeOther,
    shoreTypeQuantity,
    shoreTypeArrayQuantity,
    shoreTypeInt64,
    shoreTypeArrayInt64,
    shoreTypeNumberOfTypes
};


