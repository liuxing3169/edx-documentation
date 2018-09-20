.. _Enable Certificates:

##############################
启用课程证书
##############################

这个主题描述如何开启和配置课程证书到你的Open edX实例中。

关于配置program证书的相关信息，参考 edx/credentials GitHub 代码仓库中的文档。

.. contents::
   :local:
   :depth: 1

*********************************
课程证书概览
*********************************

组织和课程团队可以选择为那些通过一门课程的学习者生成证书。学习者可以查看，打印，或者分享他们的证书。

关于证书的其他信息，请参阅 *Building and Running an Open edX Course* 指南中的
:ref:`opencoursestaff:Setting Up Certificates` 或者 *Open edX Learner's Guide* 中的
:ref:`openlearners:Print a Web Certificate` 。

在你的Open edX安装实例上开启课程证书，你必须在Studio和LMS中开启一个功能标记，并完成这个主题中描述的配置任务。

.. Note::
  操作之前，回顾 :ref:`Guidelines for Updating the Open edX
  Platform`.

*************************************************
在Studio和LMS中开启课程证书
*************************************************

要开启证书，你需要修改 ``lms.env.json`` 和 ``cms.env.json`` 文件，它们是放在和 ``edx-platform``同一级的文件目录中的。

#. 在 ``lms.env.json`` 和 ``cms.env.json`` 文件中,将 ``FEATURES`` 中的  ``CERTIFICATES_HTML_VIEW`` 的值设置为 ``true``。

   .. code-block:: none

     "FEATURES": {
         ...
         'CERTIFICATES_HTML_VIEW': true,
         ...
     }

#. 保存 ``lms.env.json`` 和 ``cms.env.json`` 文件。

#. 如果这里不是已经存在，创建 ``/tmp/certificates`` 文件夹，用户和用户组都为 ``www-data``。具体取决于你的配置，这个文件夹可能不会在重启时被留存下来，因此可能需要通过一个脚本来创建它。

#. 运行数据库 migrations.


*****************************************
在Studio中配置课程证书
*****************************************

Within Studio, course team members with the Admin role can create and edit a
certificate configuration that is used to generate certificates for their
course, including adding signatories and images for organization logo and
signature images for signatories. For details, :ref:`opencoursestaff:Setting Up
Certificates` in *Building and Running an Open edX Course*.


**********************************************************
为你的Open edX实例配置课程证书
**********************************************************

#. Access the LMS Django Administration website for your instance of Open edX.
   To do this, go to ``https://<host name of your Open edX instance>/admin``.
   For example, this might be ``https://courses.YourOrganization.com/admin``.

#. Under **Site Administration** > **Certificates**, add an HTML View
   Configuration, and select **Enabled**.

#. Set the following certificates-related parameters for your Open edX
   instance.

   * ``platform_name``
   * ``company_about_url``
   * ``company_privacy_url``
   * ``company_tos_url``
   * ``company_verified_certificate_url``
   * ``logo_src``
   * ``logo_url``

   For each course mode for which you want to offer certificates (such as
   "honor" or "verified"), define these parameters.

   * ``certificate_type``
   * ``certificate_title``
   * ``document_body_class_append``.

   Make sure the mode name matches your course mode name exactly. An example
   follows.

   For more information about course modes, also called enrollment modes
   or enrollment tracks, see :ref:`enrollment track<enrollment_track_g>`.

   .. code-block:: none

    {
        "default": {
            "accomplishment_class_append": "accomplishment-certificate",
            "platform_name": "YourPlatformName",
            "company_about_url":"http://www.YourOrganization.com/about-us",
            "company_privacy_url": "http://www.YourOrganization.com/our-privacy-policy",
            "company_tos_url": "http://www.YourOrganization.com/our-terms-service",
            "company_verified_certificate_url": "http://www.YourOrganization.com/about_verified_certificates",
            "logo_src": "/static/certificates/images/our_logo.svg",
            "logo_url": "www.YourOrganization.com"
        },
        "honor": {
            "certificate_type": "honor",
            "certificate_title": "Honor Certificate",
            "document_body_class_append": "is-honorcode"
        },
        "verified": {
            "certificate_type": "verified",
            "certificate_title": "Verified Certificate",
            "document_body_class_append": "is-idverified"
        },
        "base": {
            "certificate_type": "base",
            "certificate_title": "Certificate of Achievement",
            "document_body_class_append": "is-base"
        },
        "distinguished": {
            "certificate_type": "distinguished",
            "certificate_title": "Distinguished Certificate of Achievement",
            "document_body_class_append": "is-distinguished"
        }
    }

#. Save the configuration parameters.

#. Restart the Studio and LMS processes to load the updated environment
   configurations.


.. _Discontinue Audit Certificates:

=====================================
停止审核跟踪证书
=====================================

Organizations that offer certificates to audit track learners who pass a
course can discontinue generation of this type of certificate. For example,
your organization makes a strategic decision to offer certificates only to
learners who select an enrollment track other than "audit". Learners can
continue to audit courses, but they no longer receive certificates.

For more information about course tracks, also called enrollment modes or
enrollment tracks, see :ref:`enrollment track<enrollment_track_g>`.

An outline of the steps you might take if your organization decides to stop
offering certificates for learners in the audit track follows.

#. Stop advertising audit track certificates for new courses.

#. Identify running courses that offer an audit track certificate and, for
   those courses, determine the course end date that is furthest in the future.

#. Select a cutoff date for generating audit track certificates that is after
   the last course end date identified in step 2.

#. Set ``AUDIT_CERT_CUTOFF_DATE`` to a date in YYYY-MM-DD format. Specifying
   this date ensures that certificates are not generated for audit track
   learners in any course after the specified date.

The ``AUDIT_CERT_CUTOFF_DATE`` feature flag affects only the generation of
audit certificates. Learners who audit courses continue to receive grades,
which are shown on the course **Progress** page.


******************************************************
为你的组织定义证书模板
******************************************************

Set up the templates for certificates that your organization will issue. Base
templates are included, but you must ensure that they are customized for your
organization. For example, you can change the images that appear on
certificates for each course mode that your organization supports, as well as
fonts and colors that are used on certificates.

To issue certificates in more than one language, see :ref:`Certificates in
Additional Languages`.

To display hours of effort on certificates, see :ref:`Display Hours of
Effort`.

Assets for HTML certificates exist in the following locations.

* ``lms/templates/certificates`` - this folder contains .html files for
  certificates. The file ``valid.html`` is an example of a certificate file.
  Files with names that start with an underscore, such as
  ``_certificate_footer.html``, are partial files that can be referenced in the
  main certificate .html files.

* ``lms/static/certificates`` - subfolders of this folder contain assets used
  in creating certificates, such as images, fonts, and sass/css files.

  .. note:: The organization logo on a certificate is uploaded in Studio. For
     details, see :ref:`opencoursestaff:Setting Up Certificates` in *Building
     and Running an Open edX Course*.



.. _Certificates in Additional Languages:

************************************************************
在附加语言中启用证书
************************************************************

You can configure course certificates to render in a specific language.

.. contents::
   :local:
   :depth: 1

=====================================================
在附加语言中配置课程证书
=====================================================

To enable generating course certificates in languages other than the
default language of your platform, follow these steps.

.. note:: Base certificate templates already exist for English and
      Spanish. If you want a course certificate that is different from the
      default certificate for the organization or language, create a new
      certificate template.

#. Add the language in which you want to generate certificates to
   ``EDXAPP_CERTIFICATE_TEMPLATE_LANGUAGES``
   (``edx/configuration/playbooks/roles/edxapp/defaults/main.yml``), where the
   key is the language code and the value is the name of the language.

   For example,    ``'fr':'français'``.

#. In the LMS Django Administration site for your instance of Open edX, under
   **Site Administration** > **Certificates** > **Certificate templates**, add
   a certificate template for each additional language in which you want to
   generate certificates.

#. In each certificate template, modify the configuration parameters as
   required to apply the template either to all course runs in an
   organization, or to a single course run.


   .. list-table::
      :widths: 10 35 35
      :header-rows: 1

      * - Parameter
        - To apply the template to all course runs
          in the organization
        - To apply the template to a specific course run
      * - ``Language``
        - Select the language that you want the certificate to be generated
          in.
        - Select the language that you want the certificate to be generated
          in.
      * - ``Organization ID``
        - Enter the ID for the organization whose courses should use this
          certificate template.
        - Select ``None``.
      * - ``Course Key``
        - Leave empty.
        - Enter the course key for the course run which should use this
          certificate template.
      * - ``Mode``
        - (Optional) Specify the course mode for which certificates will be
          generated using this template. If no mode is specified, this template
          is used for all course modes.
        - (Optional) Specify the course mode for which certificates will be
          generated using this template. If no mode is specified, this template
          is used for all course modes.
      * - ``Is Active``
        - Select this checkbox to make this template active.
        - Select this checkbox to make this template active.


   .. note:: If more than one certificate template would apply to a course
      run, the most specific (lowest level) template is used. For example, if
      you define a certificate template for all courses in an organization and
      another template for a specific course run, the template for the course
      run is used.

#. Save each certificate template.

#. ONLY if you are enabling additional language certificates for a specific
   course run, add a certificate generation course setting in LMS Django
   Administration, under **Site Administration** > **Certificates**.

#. In the **Course key** field of the certificate generation course setting,
   specify the course run for which you are enabling language specific
   certificate templates.

#. Select **Language specific templates enabled**, and save the configuration.


.. _Display Hours of Effort:

**********************************************
在课程证书上显示学时
**********************************************


To display hours of effort for a course run on a course certificate, follow
these steps.

#. Log in to the Discovery service Django Administration site for your instance
   of Open edX. To do this, go to ``https://<discovery.host name of your Open
   edX instance>/admin``. For example, this might be
   ``https://discovery.YourOrganization.com/admin``.

#. Under **Course Metadata** > **Course Runs**, locate the course run, and make
   sure there are values for the following attributes.

   * Max effort
   * Weeks to complete

#. Log in to the LMS Django Administration site for your instance of Open edX.
   To do this, go to ``https://<courses.host name of your Open edX
   instance>/admin``. For example, this might be
   ``https://courses.YourOrganization.com/admin``.

#. Under **Site Administration** > **Certificates**, add or edit a
   certificate generation course setting.

#. Select ``Yes`` for **Include hours of effort** and save the configuration.

#. Under **Site Administration** > **Certificates**, add or edit a certificate
   template.

#. In the certificate template, ensure that a ``div`` element exists that
   includes the context variable ``hours_of_effort``.

#. Save your edits to the certificate template.


.. _Generate Certificates for a Course:

*****************************************
为一门课程生成证书
*****************************************

To generate certificates for a course, run the ``manage.py`` script with the
following settings. When the script finishes running, grades are calculated
for learners who are enrolled in the course, and certificates are generated
for eligible learners.

#. Obtain the course ID for the course for which you are generating
   certificates. When you view course content in your browser, the course ID
   appears as part of the URL. For example, in the URL
   ``http://www.edx.org/course/course-v1:edX+demoX_Demo_2015``, the course ID
   is ``course-v1:edX+demoX_Demo_2015``. For some courses, the course ID
   contains slashes. For example, ``edX/Demox/Demo_2014``.

#. Run ``manage.py`` with the following settings, replacing ``{CourseID}``
   with the actual course ID. Do not include beginning or trailing slashes.

   ``./manage.py lms --settings=aws ungenerated_certs -c {CourseID}``

   For example,

   ``./manage.py lms --settings=aws ungenerated_certs -c course-v1:edX+demoX_Demo_2015``.

   .. Note::
     If the LMS is running on a server that does not have https support (such
     as a locally run fullstack for testing) you will need to use the
     ``--insecure`` flag so that the certificate generation service contacts
     the LMS on http instead of on https.

#. View the certificate generation status for a course using
   ``gen_cert_report``. An example follows.

   ``./manage.py lms --settings=aws gen_cert_report -c course-v1:edX+demoX_Demo_2015``.

.. include:: ../../../links/links.rst
