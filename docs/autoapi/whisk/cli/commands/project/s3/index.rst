:mod:`whisk.cli.commands.project.s3`
====================================

.. py:module:: whisk.cli.commands.project.s3


Module Contents
---------------


.. data:: project
   

   

.. function:: cli()


.. function:: create(bucket)

   Creates an S3 bucket to store data. If no bucket name is provided, the bucket name is generated from the project directory name.


.. function:: delete(bucket)

   Delete the S3 bucket used for data storage. If no bucket name is provided, the bucket name is generated from the project directory name.


