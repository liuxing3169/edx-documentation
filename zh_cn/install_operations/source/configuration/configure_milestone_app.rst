
.. for reuse, not in TOC, excluded from build list

************************************
配置里程碑应用程序
************************************

#. Set the value of ``MILESTONES_APP`` in the ``lms.env.json`` and
   ``cms.env.json`` files to ``True``.

   .. code-block:: none

       # Milestones application flag
       'MILESTONES_APP': True,

#. Save the the ``lms.env.json`` and ``cms.env.json`` files.

#. Run database migrations.
