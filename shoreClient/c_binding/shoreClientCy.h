/* Generated by Cython 0.23.4 */

#ifndef __PYX_HAVE__shoreClientCy
#define __PYX_HAVE__shoreClientCy


#ifndef __PYX_HAVE_API__shoreClientCy

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#ifndef DL_IMPORT
  #define DL_IMPORT(_T) _T
#endif

__PYX_EXTERN_C DL_IMPORT(void) shorePutCy(char const *, char const *, unsigned int const , unsigned int const , unsigned int const *, int const , void const *);
__PYX_EXTERN_C DL_IMPORT(void) shoreGetCy(char const *, char const *, unsigned int const , unsigned int const , unsigned int *, int *, void *);
__PYX_EXTERN_C DL_IMPORT(int) shoreQueryCy(char const *, char const *, unsigned int *, unsigned int *, int *);
__PYX_EXTERN_C DL_IMPORT(void) shoreZmqInitCy(void);

#endif /* !__PYX_HAVE_API__shoreClientCy */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initshoreClientCy(void);
#else
PyMODINIT_FUNC PyInit_shoreClientCy(void);
#endif

#endif /* !__PYX_HAVE__shoreClientCy */
