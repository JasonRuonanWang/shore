#ifndef __PYX_HAVE__c_client
#define __PYX_HAVE__c_client


#ifndef __PYX_HAVE_API__c_client

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

__PYX_EXTERN_C DL_IMPORT(void) shorePut(void);

#endif /* !__PYX_HAVE_API__c_client */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initc_client(void);
#else
PyMODINIT_FUNC PyInit_c_client(void);
#endif

#endif /* !__PYX_HAVE__c_client */
