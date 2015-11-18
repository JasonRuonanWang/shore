#ifndef __PYX_HAVE__shoreClient
#define __PYX_HAVE__shoreClient


#ifndef __PYX_HAVE_API__shoreClient

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

__PYX_EXTERN_C DL_IMPORT(void) shorePut(char const *, char const *, unsigned int, unsigned int *, void *);

#endif /* !__PYX_HAVE_API__shoreClient */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initshoreClient(void);
#else
PyMODINIT_FUNC PyInit_shoreClient(void);
#endif

#endif /* !__PYX_HAVE__shoreClient */
