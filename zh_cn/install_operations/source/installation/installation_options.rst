.. _Open edX Platform Installation Options:

########################################
Open edX Platform 安装选项
########################################

这个章节描述了Open edX安装选项和每个不同选项所包含的组件。这里有两种开发环境安装选项，可以使用Docker安装Open edX软件。
如果你喜欢，你可以使用Native安装的方法安装到一台你自己的Ubuntu机器中。

.. contents::
 :local:
 :depth: 1

**********************************
Open edX Platform on Docker
**********************************

你可以安装Open edX开发者技术栈 (**Devstack**) 或者 Open edX analytics 开发者技术栈 (**Analytics Devstack**).

* Devstack 是为本地开发设计的一组Docker容器。了解更多信息，请参阅 :ref:`Info Devstack`.

* Analytics Devstack 是一个修改过的版本的Devstack安装，可以允许你运行Open edX Analytics. 了解更多信息, 请参阅 :ref:`Info Analytics Devstack`.

你可以在Linux或macOS上运行Devstack或Analytics Devstack。查看 `Docker`_ 下载页面了解你可以运行Docker关于操作系统和架构的相关信息.

Devstack using `Docker for Windows`_ has not been tested and it is not
supported.

.. _Info Devstack:

=================
Open edX Devstack
=================

Devstack is a deployment of the Open edX platform within a set of Docker
containers designed for local development. Running the Open edX platform
locally allows you to discover and fix system configuration issues early in
development.

Devstack simplifies certain production settings to make development more
convenient. For example, `nginx`_ and `gunicorn`_ are disabled in Devstack;
Devstack uses Django's ``runserver`` instead.

.. note::
  Because of the large number of dependencies needed to develop extensions to
  Open edX Insights, a separate development environment is available to support
  Analytics development. For more information, see :ref:`Installing and
  Starting Analytics Devstack`.

For more information about Docker, see the `Docker documentation`_.

.. _Info Analytics Devstack:

===========================
Open edX Analytics Devstack
===========================

Some users might want to develop Analytics features on their instance of the
Open edX platform. Because of the large number of dependencies needed to
develop extensions to Analytics, edX has created a separate developer stack,
known as Analytics Devstack. We strongly recommend that you install the
Analytics Devstack instead of adding Analytics extensions to an instance of
devstack.

Analytics Devstack is a modified version of the :ref:`Open edX developer
stack<Info Devstack>`. This development environment provides all of the
services and tools needed to modify the Open edX Analytics Pipeline, Data API,
and Insights projects.


*******************
Native Installation
*******************

The Native installation installs the Open edX software on your own Ubuntu 16.04
machine in a production-like configuration. Details are at the `Open edX
Native Installation`_ page on the edX wiki.


*******************
软件组件
*******************

一个Devstack安装包括下列的Open edX组件：

* 学习管理系统 (LMS)
* Open edX Studio
* 论坛
* Open Response Assessments (ORA)
* E-Commerce
* 证书
* 笔记
* 课程发现
* XQueue
* Open edX 搜索
* A demonstration Open edX course

Analytics Devstack also includes the following Open edX components:

* Open edX Analytics Data API
* Open edX Insights
* The components needed to run the Open edX Analytics Pipeline. This is the
  primary extract, transform, and load (ETL) tool that extracts and analyzes
  data from the other Open edX services.


.. include:: ../../../links/links.rst
