SHORE is a middleware framework designed to facilitate the implementation of
plugins to support a range of storage and I/O interfaces on the backend side
and a range of data format plugins on the frontend side. This allows a
separation of I/O optimisation from application optimisation. SHORE has been
desinged and implemented as part of a PhD thesis and is thus not production
ready software, but more a proof of concept which in fact has been used and
deployed for real-world science data reduction on very large scales.

SHORE is not an acronym, but can be loosely interpreted as Storage Hierarchy 
Optimization and Retrieval Environment. The idea of SHORE comes from the scene 
where waves hit a seashore and disappear in the sand grains. This is similar to 
a piece of data 'disappearing' in some storage. The concept of the shoreline 
is the interface between the ocean (data) and land (storage). A shoreline 
extending to distance represents a horizontally scalable data I/O interface.

When a wave hits the shore, water fills from top down. Similarly, in a data 
ingestion process, storage hierarchies with higher throughput are usually 
desired first. Then data is moved to slower hierarchies when faster ones are 
filled up. Sand grains represent plugins for a certain data format or type. 
The poles of a jetty going out into the sea are sensors picking up the dynamics
and type (data type) of the water (data) before it hits the shoreline, informing 
the shoreline where to finally put the water (which plugins to use).

Waves (data ingestion) can also come in different intensities, high 
(intensive) ones and low (sparse) ones. In order to handle each type in the 
optimal way, there needs a data-aware plugin infrastructure, to make decisions 
dynamically based on characteristics of a data ingestion. In the opposite 
direction, a storage-aware infrastructure (jetty) is also necessary to 
provide the data object (wave) with storage hierarchy (land) information before 
the ingestion happens. Apart from the main architecture, there are also concepts 
for optional functionality, such as shells, which provide the in-situ data 
processing ability.
