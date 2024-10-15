from __future__ import annotations

# pylint: disable=too-many-lines
types: list[str] = [
    "AMZN::SDC::Deployment",
    "AWS::ACMPCA::Certificate",
    "AWS::ACMPCA::CertificateAuthority",
    "AWS::ACMPCA::CertificateAuthorityActivation",
    "AWS::ACMPCA::Permission",
    "AWS::ARCZonalShift::AutoshiftObserverNotificationStatus",
    "AWS::ARCZonalShift::ZonalAutoshiftConfiguration",
    "AWS::AccessAnalyzer::Analyzer",
    "AWS::AmazonMQ::Broker",
    "AWS::AmazonMQ::Configuration",
    "AWS::AmazonMQ::ConfigurationAssociation",
    "AWS::ApiGateway::Account",
    "AWS::ApiGateway::ApiKey",
    "AWS::ApiGateway::Authorizer",
    "AWS::ApiGateway::BasePathMapping",
    "AWS::ApiGateway::ClientCertificate",
    "AWS::ApiGateway::Deployment",
    "AWS::ApiGateway::DocumentationPart",
    "AWS::ApiGateway::DocumentationVersion",
    "AWS::ApiGateway::DomainName",
    "AWS::ApiGateway::GatewayResponse",
    "AWS::ApiGateway::Method",
    "AWS::ApiGateway::Model",
    "AWS::ApiGateway::RequestValidator",
    "AWS::ApiGateway::Resource",
    "AWS::ApiGateway::RestApi",
    "AWS::ApiGateway::Stage",
    "AWS::ApiGateway::UsagePlan",
    "AWS::ApiGateway::UsagePlanKey",
    "AWS::ApiGatewayV2::Api",
    "AWS::ApiGatewayV2::ApiMapping",
    "AWS::ApiGatewayV2::Authorizer",
    "AWS::ApiGatewayV2::Deployment",
    "AWS::ApiGatewayV2::DomainName",
    "AWS::ApiGatewayV2::Integration",
    "AWS::ApiGatewayV2::IntegrationResponse",
    "AWS::ApiGatewayV2::Model",
    "AWS::ApiGatewayV2::Route",
    "AWS::ApiGatewayV2::RouteResponse",
    "AWS::ApiGatewayV2::Stage",
    "AWS::AppConfig::Application",
    "AWS::AppConfig::ConfigurationProfile",
    "AWS::AppConfig::Deployment",
    "AWS::AppConfig::DeploymentStrategy",
    "AWS::AppConfig::Environment",
    "AWS::AppConfig::Extension",
    "AWS::AppConfig::ExtensionAssociation",
    "AWS::AppConfig::HostedConfigurationVersion",
    "AWS::ApplicationAutoScaling::ScalableTarget",
    "AWS::ApplicationAutoScaling::ScalingPolicy",
    "AWS::Athena::DataCatalog",
    "AWS::Athena::NamedQuery",
    "AWS::Athena::PreparedStatement",
    "AWS::Athena::WorkGroup",
    "AWS::AutoScaling::AutoScalingGroup",
    "AWS::AutoScaling::LaunchConfiguration",
    "AWS::AutoScaling::LifecycleHook",
    "AWS::AutoScaling::ScalingPolicy",
    "AWS::AutoScaling::ScheduledAction",
    "AWS::AutoScaling::WarmPool",
    "AWS::Backup::BackupPlan",
    "AWS::Backup::BackupSelection",
    "AWS::Backup::BackupVault",
    "AWS::Batch::ComputeEnvironment",
    "AWS::Batch::JobDefinition",
    "AWS::Batch::JobQueue",
    "AWS::Batch::SchedulingPolicy",
    "AWS::CDK::Metadata",
    "AWS::CE::AnomalyMonitor",
    "AWS::CE::AnomalySubscription",
    "AWS::CertificateManager::Certificate",
    "AWS::Chatbot::MicrosoftTeamsChannelConfiguration",
    "AWS::Chatbot::SlackChannelConfiguration",
    "AWS::CloudFormation::CustomResource",
    "AWS::CloudFormation::HookDefaultVersion",
    "AWS::CloudFormation::HookTypeConfig",
    "AWS::CloudFormation::HookVersion",
    "AWS::CloudFormation::Macro",
    "AWS::CloudFormation::PublicTypeVersion",
    "AWS::CloudFormation::ResourceDefaultVersion",
    "AWS::CloudFormation::ResourceVersion",
    "AWS::CloudFormation::Stack",
    "AWS::CloudFormation::StackSet",
    "AWS::CloudFormation::WaitCondition",
    "AWS::CloudFormation::WaitConditionHandle",
    "AWS::CloudFront::CachePolicy",
    "AWS::CloudFront::CloudFrontOriginAccessIdentity",
    "AWS::CloudFront::ContinuousDeploymentPolicy",
    "AWS::CloudFront::Distribution",
    "AWS::CloudFront::Function",
    "AWS::CloudFront::KeyGroup",
    "AWS::CloudFront::KeyValueStore",
    "AWS::CloudFront::MonitoringSubscription",
    "AWS::CloudFront::OriginAccessControl",
    "AWS::CloudFront::OriginRequestPolicy",
    "AWS::CloudFront::PublicKey",
    "AWS::CloudFront::RealtimeLogConfig",
    "AWS::CloudFront::ResponseHeadersPolicy",
    "AWS::CloudTrail::Trail",
    "AWS::CloudWatch::Alarm",
    "AWS::CloudWatch::AnomalyDetector",
    "AWS::CloudWatch::CompositeAlarm",
    "AWS::CloudWatch::Dashboard",
    "AWS::CloudWatch::InsightRule",
    "AWS::CloudWatch::MetricStream",
    "AWS::CodeDeploy::Application",
    "AWS::CodeDeploy::DeploymentConfig",
    "AWS::CodeDeploy::DeploymentGroup",
    "AWS::CodePipeline::CustomActionType",
    "AWS::CodePipeline::Pipeline",
    "AWS::Cognito::IdentityPool",
    "AWS::Cognito::IdentityPoolPrincipalTag",
    "AWS::Cognito::IdentityPoolRoleAttachment",
    "AWS::Cognito::LogDeliveryConfiguration",
    "AWS::Cognito::UserPool",
    "AWS::Cognito::UserPoolClient",
    "AWS::Cognito::UserPoolGroup",
    "AWS::Cognito::UserPoolResourceServer",
    "AWS::Cognito::UserPoolRiskConfigurationAttachment",
    "AWS::Cognito::UserPoolUICustomizationAttachment",
    "AWS::Cognito::UserPoolUser",
    "AWS::Cognito::UserPoolUserToGroupAttachment",
    "AWS::Config::AggregationAuthorization",
    "AWS::Config::ConfigRule",
    "AWS::Config::ConfigurationAggregator",
    "AWS::Config::ConfigurationRecorder",
    "AWS::Config::ConformancePack",
    "AWS::Config::DeliveryChannel",
    "AWS::Config::OrganizationConfigRule",
    "AWS::Config::OrganizationConformancePack",
    "AWS::Config::RemediationConfiguration",
    "AWS::Config::StoredQuery",
    "AWS::ControlTower::EnabledBaseline",
    "AWS::ControlTower::EnabledControl",
    "AWS::ControlTower::LandingZone",
    "AWS::DLM::LifecyclePolicy",
    "AWS::DMS::DataProvider",
    "AWS::DMS::InstanceProfile",
    "AWS::DMS::MigrationProject",
    "AWS::DMS::ReplicationConfig",
    "AWS::DataPipeline::Pipeline",
    "AWS::DataSync::Agent",
    "AWS::DataSync::LocationAzureBlob",
    "AWS::DataSync::LocationEFS",
    "AWS::DataSync::LocationFSxLustre",
    "AWS::DataSync::LocationFSxONTAP",
    "AWS::DataSync::LocationFSxOpenZFS",
    "AWS::DataSync::LocationFSxWindows",
    "AWS::DataSync::LocationHDFS",
    "AWS::DataSync::LocationNFS",
    "AWS::DataSync::LocationObjectStorage",
    "AWS::DataSync::LocationS3",
    "AWS::DataSync::LocationSMB",
    "AWS::DataSync::Task",
    "AWS::DirectoryService::MicrosoftAD",
    "AWS::DirectoryService::SimpleAD",
    "AWS::DynamoDB::GlobalTable",
    "AWS::DynamoDB::Table",
    "AWS::EC2::CapacityReservation",
    "AWS::EC2::CapacityReservationFleet",
    "AWS::EC2::CustomerGateway",
    "AWS::EC2::DHCPOptions",
    "AWS::EC2::EC2Fleet",
    "AWS::EC2::EIP",
    "AWS::EC2::EIPAssociation",
    "AWS::EC2::EgressOnlyInternetGateway",
    "AWS::EC2::FlowLog",
    "AWS::EC2::GatewayRouteTableAssociation",
    "AWS::EC2::Host",
    "AWS::EC2::IPAM",
    "AWS::EC2::IPAMAllocation",
    "AWS::EC2::IPAMPool",
    "AWS::EC2::IPAMPoolCidr",
    "AWS::EC2::IPAMResourceDiscovery",
    "AWS::EC2::IPAMResourceDiscoveryAssociation",
    "AWS::EC2::IPAMScope",
    "AWS::EC2::Instance",
    "AWS::EC2::InternetGateway",
    "AWS::EC2::KeyPair",
    "AWS::EC2::LaunchTemplate",
    "AWS::EC2::NatGateway",
    "AWS::EC2::NetworkAcl",
    "AWS::EC2::NetworkAclEntry",
    "AWS::EC2::NetworkInterface",
    "AWS::EC2::NetworkInterfaceAttachment",
    "AWS::EC2::NetworkInterfacePermission",
    "AWS::EC2::PlacementGroup",
    "AWS::EC2::PrefixList",
    "AWS::EC2::Route",
    "AWS::EC2::RouteTable",
    "AWS::EC2::SecurityGroup",
    "AWS::EC2::SecurityGroupEgress",
    "AWS::EC2::SecurityGroupIngress",
    "AWS::EC2::SnapshotBlockPublicAccess",
    "AWS::EC2::SpotFleet",
    "AWS::EC2::Subnet",
    "AWS::EC2::SubnetCidrBlock",
    "AWS::EC2::SubnetNetworkAclAssociation",
    "AWS::EC2::SubnetRouteTableAssociation",
    "AWS::EC2::TrafficMirrorFilter",
    "AWS::EC2::TrafficMirrorFilterRule",
    "AWS::EC2::TrafficMirrorSession",
    "AWS::EC2::TrafficMirrorTarget",
    "AWS::EC2::TransitGateway",
    "AWS::EC2::TransitGatewayAttachment",
    "AWS::EC2::TransitGatewayConnect",
    "AWS::EC2::TransitGatewayMulticastDomain",
    "AWS::EC2::TransitGatewayMulticastDomainAssociation",
    "AWS::EC2::TransitGatewayMulticastGroupMember",
    "AWS::EC2::TransitGatewayMulticastGroupSource",
    "AWS::EC2::TransitGatewayPeeringAttachment",
    "AWS::EC2::TransitGatewayRoute",
    "AWS::EC2::TransitGatewayRouteTable",
    "AWS::EC2::TransitGatewayRouteTableAssociation",
    "AWS::EC2::TransitGatewayRouteTablePropagation",
    "AWS::EC2::TransitGatewayVpcAttachment",
    "AWS::EC2::VPC",
    "AWS::EC2::VPCCidrBlock",
    "AWS::EC2::VPCDHCPOptionsAssociation",
    "AWS::EC2::VPCEndpoint",
    "AWS::EC2::VPCEndpointConnectionNotification",
    "AWS::EC2::VPCEndpointService",
    "AWS::EC2::VPCEndpointServicePermissions",
    "AWS::EC2::VPCGatewayAttachment",
    "AWS::EC2::VPCPeeringConnection",
    "AWS::EC2::VPNConnection",
    "AWS::EC2::VPNConnectionRoute",
    "AWS::EC2::VPNGateway",
    "AWS::EC2::VPNGatewayRoutePropagation",
    "AWS::EC2::Volume",
    "AWS::EC2::VolumeAttachment",
    "AWS::ECR::PullThroughCacheRule",
    "AWS::ECR::RegistryPolicy",
    "AWS::ECR::ReplicationConfiguration",
    "AWS::ECR::Repository",
    "AWS::ECR::RepositoryCreationTemplate",
    "AWS::ECS::CapacityProvider",
    "AWS::ECS::Cluster",
    "AWS::ECS::ClusterCapacityProviderAssociations",
    "AWS::ECS::PrimaryTaskSet",
    "AWS::ECS::Service",
    "AWS::ECS::TaskDefinition",
    "AWS::ECS::TaskSet",
    "AWS::EFS::AccessPoint",
    "AWS::EFS::FileSystem",
    "AWS::EFS::MountTarget",
    "AWS::EKS::AccessEntry",
    "AWS::EKS::Addon",
    "AWS::EKS::Cluster",
    "AWS::EKS::FargateProfile",
    "AWS::EKS::IdentityProviderConfig",
    "AWS::EKS::Nodegroup",
    "AWS::EKS::PodIdentityAssociation",
    "AWS::EMR::Cluster",
    "AWS::EMR::InstanceFleetConfig",
    "AWS::EMR::InstanceGroupConfig",
    "AWS::EMR::SecurityConfiguration",
    "AWS::EMR::Step",
    "AWS::ElastiCache::CacheCluster",
    "AWS::ElastiCache::ParameterGroup",
    "AWS::ElastiCache::ReplicationGroup",
    "AWS::ElastiCache::SecurityGroup",
    "AWS::ElastiCache::SecurityGroupIngress",
    "AWS::ElastiCache::ServerlessCache",
    "AWS::ElastiCache::SubnetGroup",
    "AWS::ElastiCache::User",
    "AWS::ElastiCache::UserGroup",
    "AWS::ElasticBeanstalk::Application",
    "AWS::ElasticBeanstalk::ApplicationVersion",
    "AWS::ElasticBeanstalk::ConfigurationTemplate",
    "AWS::ElasticBeanstalk::Environment",
    "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::ElasticLoadBalancingV2::Listener",
    "AWS::ElasticLoadBalancingV2::ListenerCertificate",
    "AWS::ElasticLoadBalancingV2::ListenerRule",
    "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "AWS::ElasticLoadBalancingV2::TargetGroup",
    "AWS::Elasticsearch::Domain",
    "AWS::Events::EventBus",
    "AWS::Events::EventBusPolicy",
    "AWS::Events::Rule",
    "AWS::FMS::NotificationChannel",
    "AWS::FMS::Policy",
    "AWS::FSx::DataRepositoryAssociation",
    "AWS::FSx::FileSystem",
    "AWS::FSx::Snapshot",
    "AWS::FSx::StorageVirtualMachine",
    "AWS::FSx::Volume",
    "AWS::GameLift::Alias",
    "AWS::GameLift::Build",
    "AWS::GameLift::Fleet",
    "AWS::GlobalAccelerator::Accelerator",
    "AWS::GlobalAccelerator::CrossAccountAttachment",
    "AWS::GlobalAccelerator::EndpointGroup",
    "AWS::GlobalAccelerator::Listener",
    "AWS::Glue::Classifier",
    "AWS::Glue::Connection",
    "AWS::Glue::Crawler",
    "AWS::Glue::CustomEntityType",
    "AWS::Glue::DataCatalogEncryptionSettings",
    "AWS::Glue::DataQualityRuleset",
    "AWS::Glue::Database",
    "AWS::Glue::DevEndpoint",
    "AWS::Glue::Job",
    "AWS::Glue::MLTransform",
    "AWS::Glue::Partition",
    "AWS::Glue::SecurityConfiguration",
    "AWS::Glue::Table",
    "AWS::Glue::Trigger",
    "AWS::Glue::Workflow",
    "AWS::GuardDuty::Detector",
    "AWS::GuardDuty::Filter",
    "AWS::GuardDuty::IPSet",
    "AWS::GuardDuty::MalwareProtectionPlan",
    "AWS::GuardDuty::Master",
    "AWS::GuardDuty::Member",
    "AWS::GuardDuty::ThreatIntelSet",
    "AWS::IAM::AccessKey",
    "AWS::IAM::Group",
    "AWS::IAM::GroupPolicy",
    "AWS::IAM::InstanceProfile",
    "AWS::IAM::ManagedPolicy",
    "AWS::IAM::OIDCProvider",
    "AWS::IAM::Policy",
    "AWS::IAM::Role",
    "AWS::IAM::RolePolicy",
    "AWS::IAM::SAMLProvider",
    "AWS::IAM::ServerCertificate",
    "AWS::IAM::ServiceLinkedRole",
    "AWS::IAM::User",
    "AWS::IAM::UserPolicy",
    "AWS::IAM::UserToGroupAddition",
    "AWS::IdentityStore::Group",
    "AWS::IdentityStore::GroupMembership",
    "AWS::ImageBuilder::Component",
    "AWS::ImageBuilder::ContainerRecipe",
    "AWS::ImageBuilder::DistributionConfiguration",
    "AWS::ImageBuilder::Image",
    "AWS::ImageBuilder::ImagePipeline",
    "AWS::ImageBuilder::ImageRecipe",
    "AWS::ImageBuilder::InfrastructureConfiguration",
    "AWS::ImageBuilder::Workflow",
    "AWS::IoT::Certificate",
    "AWS::IoT::Policy",
    "AWS::IoT::PolicyPrincipalAttachment",
    "AWS::IoT::Thing",
    "AWS::IoT::ThingPrincipalAttachment",
    "AWS::IoT::TopicRule",
    "AWS::KMS::Alias",
    "AWS::KMS::Key",
    "AWS::KMS::ReplicaKey",
    "AWS::Kinesis::Stream",
    "AWS::Kinesis::StreamConsumer",
    "AWS::KinesisAnalyticsV2::Application",
    "AWS::KinesisFirehose::DeliveryStream",
    "AWS::LakeFormation::DataCellsFilter",
    "AWS::LakeFormation::DataLakeSettings",
    "AWS::LakeFormation::Permissions",
    "AWS::LakeFormation::PrincipalPermissions",
    "AWS::LakeFormation::Resource",
    "AWS::LakeFormation::Tag",
    "AWS::LakeFormation::TagAssociation",
    "AWS::Lambda::Alias",
    "AWS::Lambda::EventInvokeConfig",
    "AWS::Lambda::EventSourceMapping",
    "AWS::Lambda::Function",
    "AWS::Lambda::LayerVersion",
    "AWS::Lambda::LayerVersionPermission",
    "AWS::Lambda::Permission",
    "AWS::Lambda::Version",
    "AWS::Logs::AccountPolicy",
    "AWS::Logs::Delivery",
    "AWS::Logs::DeliveryDestination",
    "AWS::Logs::DeliverySource",
    "AWS::Logs::Destination",
    "AWS::Logs::LogGroup",
    "AWS::Logs::LogStream",
    "AWS::Logs::MetricFilter",
    "AWS::Logs::QueryDefinition",
    "AWS::Logs::ResourcePolicy",
    "AWS::Logs::SubscriptionFilter",
    "AWS::MSK::BatchScramSecret",
    "AWS::MSK::Cluster",
    "AWS::MSK::ClusterPolicy",
    "AWS::MSK::Configuration",
    "AWS::MSK::VpcConnection",
    "AWS::MWAA::Environment",
    "AWS::NetworkFirewall::Firewall",
    "AWS::NetworkFirewall::FirewallPolicy",
    "AWS::NetworkFirewall::LoggingConfiguration",
    "AWS::NetworkFirewall::RuleGroup",
    "AWS::NetworkFirewall::TLSInspectionConfiguration",
    "AWS::NetworkManager::ConnectAttachment",
    "AWS::NetworkManager::ConnectPeer",
    "AWS::NetworkManager::CoreNetwork",
    "AWS::NetworkManager::CustomerGatewayAssociation",
    "AWS::NetworkManager::Device",
    "AWS::NetworkManager::GlobalNetwork",
    "AWS::NetworkManager::Link",
    "AWS::NetworkManager::LinkAssociation",
    "AWS::NetworkManager::Site",
    "AWS::NetworkManager::SiteToSiteVpnAttachment",
    "AWS::NetworkManager::TransitGatewayPeering",
    "AWS::NetworkManager::TransitGatewayRegistration",
    "AWS::NetworkManager::TransitGatewayRouteTableAttachment",
    "AWS::NetworkManager::VpcAttachment",
    "AWS::Oam::Link",
    "AWS::Oam::Sink",
    "AWS::OpenSearchService::Domain",
    "AWS::OpsWorks::App",
    "AWS::OpsWorks::ElasticLoadBalancerAttachment",
    "AWS::OpsWorks::Instance",
    "AWS::OpsWorks::Layer",
    "AWS::OpsWorks::Stack",
    "AWS::OpsWorks::UserProfile",
    "AWS::OpsWorks::Volume",
    "AWS::Organizations::Account",
    "AWS::Organizations::Organization",
    "AWS::Organizations::OrganizationalUnit",
    "AWS::Organizations::Policy",
    "AWS::Organizations::ResourcePolicy",
    "AWS::PCAConnectorSCEP::Challenge",
    "AWS::PCAConnectorSCEP::Connector",
    "AWS::RAM::Permission",
    "AWS::RAM::ResourceShare",
    "AWS::RDS::DBCluster",
    "AWS::RDS::DBClusterParameterGroup",
    "AWS::RDS::DBInstance",
    "AWS::RDS::DBParameterGroup",
    "AWS::RDS::DBProxy",
    "AWS::RDS::DBProxyEndpoint",
    "AWS::RDS::DBProxyTargetGroup",
    "AWS::RDS::DBSecurityGroup",
    "AWS::RDS::DBSecurityGroupIngress",
    "AWS::RDS::DBSubnetGroup",
    "AWS::RDS::EventSubscription",
    "AWS::RDS::Integration",
    "AWS::RDS::OptionGroup",
    "AWS::Redshift::Cluster",
    "AWS::Redshift::ClusterParameterGroup",
    "AWS::Redshift::ClusterSecurityGroup",
    "AWS::Redshift::ClusterSecurityGroupIngress",
    "AWS::Redshift::ClusterSubnetGroup",
    "AWS::Redshift::EndpointAccess",
    "AWS::Redshift::EndpointAuthorization",
    "AWS::Redshift::EventSubscription",
    "AWS::Redshift::ScheduledAction",
    "AWS::ResourceExplorer2::DefaultViewAssociation",
    "AWS::ResourceExplorer2::Index",
    "AWS::ResourceExplorer2::View",
    "AWS::ResourceGroups::Group",
    "AWS::RolesAnywhere::CRL",
    "AWS::RolesAnywhere::Profile",
    "AWS::RolesAnywhere::TrustAnchor",
    "AWS::Route53::DNSSEC",
    "AWS::Route53::HealthCheck",
    "AWS::Route53::HostedZone",
    "AWS::Route53::KeySigningKey",
    "AWS::Route53::RecordSet",
    "AWS::Route53::RecordSetGroup",
    "AWS::Route53Profiles::Profile",
    "AWS::Route53Profiles::ProfileAssociation",
    "AWS::Route53Profiles::ProfileResourceAssociation",
    "AWS::Route53Resolver::FirewallDomainList",
    "AWS::Route53Resolver::FirewallRuleGroup",
    "AWS::Route53Resolver::FirewallRuleGroupAssociation",
    "AWS::Route53Resolver::ResolverConfig",
    "AWS::Route53Resolver::ResolverDNSSECConfig",
    "AWS::Route53Resolver::ResolverEndpoint",
    "AWS::Route53Resolver::ResolverQueryLoggingConfig",
    "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation",
    "AWS::Route53Resolver::ResolverRule",
    "AWS::Route53Resolver::ResolverRuleAssociation",
    "AWS::S3::AccessPoint",
    "AWS::S3::Bucket",
    "AWS::S3::BucketPolicy",
    "AWS::S3ObjectLambda::AccessPoint",
    "AWS::S3ObjectLambda::AccessPointPolicy",
    "AWS::SDB::Domain",
    "AWS::SNS::Subscription",
    "AWS::SNS::Topic",
    "AWS::SNS::TopicInlinePolicy",
    "AWS::SNS::TopicPolicy",
    "AWS::SQS::Queue",
    "AWS::SQS::QueueInlinePolicy",
    "AWS::SQS::QueuePolicy",
    "AWS::SSM::Association",
    "AWS::SSM::Document",
    "AWS::SSM::MaintenanceWindow",
    "AWS::SSM::MaintenanceWindowTarget",
    "AWS::SSM::MaintenanceWindowTask",
    "AWS::SSM::Parameter",
    "AWS::SSM::PatchBaseline",
    "AWS::SSM::ResourceDataSync",
    "AWS::SSO::Application",
    "AWS::SSO::ApplicationAssignment",
    "AWS::SSO::Assignment",
    "AWS::SSO::Instance",
    "AWS::SSO::InstanceAccessControlAttributeConfiguration",
    "AWS::SSO::PermissionSet",
    "AWS::SageMaker::MlflowTrackingServer",
    "AWS::SageMaker::ModelCard",
    "AWS::SageMaker::ModelPackage",
    "AWS::SageMaker::ModelPackageGroup",
    "AWS::SecretsManager::ResourcePolicy",
    "AWS::SecretsManager::RotationSchedule",
    "AWS::SecretsManager::Secret",
    "AWS::SecretsManager::SecretTargetAttachment",
    "AWS::SecurityHub::AutomationRule",
    "AWS::SecurityHub::DelegatedAdmin",
    "AWS::SecurityHub::Hub",
    "AWS::SecurityHub::Insight",
    "AWS::SecurityHub::OrganizationConfiguration",
    "AWS::SecurityHub::ProductSubscription",
    "AWS::SecurityHub::SecurityControl",
    "AWS::SecurityHub::Standard",
    "AWS::ServiceCatalogAppRegistry::Application",
    "AWS::ServiceCatalogAppRegistry::AttributeGroup",
    "AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation",
    "AWS::ServiceCatalogAppRegistry::ResourceAssociation",
    "AWS::ServiceDiscovery::HttpNamespace",
    "AWS::ServiceDiscovery::Instance",
    "AWS::ServiceDiscovery::PrivateDnsNamespace",
    "AWS::ServiceDiscovery::PublicDnsNamespace",
    "AWS::ServiceDiscovery::Service",
    "AWS::Shield::DRTAccess",
    "AWS::Shield::ProactiveEngagement",
    "AWS::Shield::Protection",
    "AWS::Shield::ProtectionGroup",
    "AWS::StepFunctions::Activity",
    "AWS::StepFunctions::StateMachine",
    "AWS::StepFunctions::StateMachineAlias",
    "AWS::StepFunctions::StateMachineVersion",
    "AWS::Synthetics::Canary",
    "AWS::Transfer::Agreement",
    "AWS::Transfer::Certificate",
    "AWS::Transfer::Connector",
    "AWS::Transfer::Profile",
    "AWS::Transfer::Server",
    "AWS::Transfer::User",
    "AWS::Transfer::Workflow",
    "AWS::VerifiedPermissions::Policy",
    "AWS::VerifiedPermissions::PolicyStore",
    "AWS::VerifiedPermissions::PolicyTemplate",
    "AWS::WAF::ByteMatchSet",
    "AWS::WAF::IPSet",
    "AWS::WAF::Rule",
    "AWS::WAF::SizeConstraintSet",
    "AWS::WAF::SqlInjectionMatchSet",
    "AWS::WAF::WebACL",
    "AWS::WAF::XssMatchSet",
    "AWS::WAFv2::IPSet",
    "AWS::WAFv2::LoggingConfiguration",
    "AWS::WAFv2::RegexPatternSet",
    "AWS::WAFv2::RuleGroup",
    "AWS::WAFv2::WebACL",
    "AWS::WAFv2::WebACLAssociation",
    "AWS::WorkSpaces::Workspace",
    "AWS::XRay::Group",
    "AWS::XRay::ResourcePolicy",
    "AWS::XRay::SamplingRule",
    "Module",
]

# pylint: disable=too-many-lines
cached: list[str] = [
    "Module",
    "aws-accessanalyzer-analyzer.json",
    "aws-acmpca-certificate.json",
    "aws-acmpca-certificateauthority.json",
    "aws-acmpca-certificateauthorityactivation.json",
    "aws-acmpca-permission.json",
    "aws-amazonmq-broker.json",
    "aws-amazonmq-configuration.json",
    "aws-apigatewayv2-api.json",
    "aws-apigatewayv2-apimapping.json",
    "aws-apigatewayv2-authorizer.json",
    "aws-apigatewayv2-deployment.json",
    "aws-apigatewayv2-domainname.json",
    "aws-apigatewayv2-integration.json",
    "aws-apigatewayv2-integrationresponse.json",
    "aws-apigatewayv2-model.json",
    "aws-apigatewayv2-route.json",
    "aws-apigatewayv2-routeresponse.json",
    "aws-apigatewayv2-stage.json",
    "aws-appconfig-application.json",
    "aws-appconfig-configurationprofile.json",
    "aws-appconfig-deployment.json",
    "aws-appconfig-deploymentstrategy.json",
    "aws-appconfig-environment.json",
    "aws-appconfig-extension.json",
    "aws-appconfig-extensionassociation.json",
    "aws-appconfig-hostedconfigurationversion.json",
    "aws-arczonalshift-autoshiftobservernotificationstatus.json",
    "aws-arczonalshift-zonalautoshiftconfiguration.json",
    "aws-athena-datacatalog.json",
    "aws-athena-namedquery.json",
    "aws-athena-preparedstatement.json",
    "aws-athena-workgroup.json",
    "aws-autoscaling-autoscalinggroup.json",
    "aws-autoscaling-warmpool.json",
    "aws-backup-backupplan.json",
    "aws-backup-backupselection.json",
    "aws-backup-backupvault.json",
    "aws-batch-computeenvironment.json",
    "aws-batch-jobqueue.json",
    "aws-batch-schedulingpolicy.json",
    "aws-ce-anomalymonitor.json",
    "aws-ce-anomalysubscription.json",
    "aws-certificatemanager-certificate.json",
    "aws-chatbot-microsoftteamschannelconfiguration.json",
    "aws-chatbot-slackchannelconfiguration.json",
    "aws-cloudformation-customresource.json",
    "aws-cloudformation-hookdefaultversion.json",
    "aws-cloudformation-hooktypeconfig.json",
    "aws-cloudformation-hookversion.json",
    "aws-cloudformation-macro.json",
    "aws-cloudformation-publictypeversion.json",
    "aws-cloudformation-resourcedefaultversion.json",
    "aws-cloudformation-resourceversion.json",
    "aws-cloudformation-stackset.json",
    "aws-cloudformation-waitconditionhandle.json",
    "aws-cloudfront-cachepolicy.json",
    "aws-cloudfront-cloudfrontoriginaccessidentity.json",
    "aws-cloudfront-continuousdeploymentpolicy.json",
    "aws-cloudfront-distribution.json",
    "aws-cloudfront-function.json",
    "aws-cloudfront-keygroup.json",
    "aws-cloudfront-keyvaluestore.json",
    "aws-cloudfront-monitoringsubscription.json",
    "aws-cloudfront-originaccesscontrol.json",
    "aws-cloudfront-originrequestpolicy.json",
    "aws-cloudfront-publickey.json",
    "aws-cloudfront-realtimelogconfig.json",
    "aws-cloudfront-responseheaderspolicy.json",
    "aws-cloudtrail-trail.json",
    "aws-cloudwatch-alarm.json",
    "aws-cloudwatch-anomalydetector.json",
    "aws-cloudwatch-compositealarm.json",
    "aws-cloudwatch-dashboard.json",
    "aws-cloudwatch-insightrule.json",
    "aws-cloudwatch-metricstream.json",
    "aws-codedeploy-application.json",
    "aws-codedeploy-deploymentconfig.json",
    "aws-codedeploy-deploymentgroup.json",
    "aws-cognito-identitypool.json",
    "aws-cognito-identitypoolprincipaltag.json",
    "aws-cognito-identitypoolroleattachment.json",
    "aws-cognito-logdeliveryconfiguration.json",
    "aws-cognito-userpool.json",
    "aws-cognito-userpoolclient.json",
    "aws-cognito-userpoolgroup.json",
    "aws-cognito-userpoolresourceserver.json",
    "aws-cognito-userpoolriskconfigurationattachment.json",
    "aws-cognito-userpooluicustomizationattachment.json",
    "aws-cognito-userpooluser.json",
    "aws-cognito-userpoolusertogroupattachment.json",
    "aws-config-aggregationauthorization.json",
    "aws-config-configurationaggregator.json",
    "aws-config-configurationrecorder.json",
    "aws-config-conformancepack.json",
    "aws-config-deliverychannel.json",
    "aws-config-organizationconfigrule.json",
    "aws-config-organizationconformancepack.json",
    "aws-config-remediationconfiguration.json",
    "aws-config-storedquery.json",
    "aws-controltower-enabledbaseline.json",
    "aws-controltower-enabledcontrol.json",
    "aws-controltower-landingzone.json",
    "aws-datasync-agent.json",
    "aws-datasync-locationazureblob.json",
    "aws-datasync-locationefs.json",
    "aws-datasync-locationfsxlustre.json",
    "aws-datasync-locationfsxontap.json",
    "aws-datasync-locationfsxopenzfs.json",
    "aws-datasync-locationfsxwindows.json",
    "aws-datasync-locationhdfs.json",
    "aws-datasync-locationnfs.json",
    "aws-datasync-locationobjectstorage.json",
    "aws-datasync-locations3.json",
    "aws-datasync-locationsmb.json",
    "aws-datasync-task.json",
    "aws-dlm-lifecyclepolicy.json",
    "aws-dms-dataprovider.json",
    "aws-dms-instanceprofile.json",
    "aws-dms-migrationproject.json",
    "aws-dms-replicationconfig.json",
    "aws-dynamodb-globaltable.json",
    "aws-dynamodb-table.json",
    "aws-ec2-capacityreservation.json",
    "aws-ec2-capacityreservationfleet.json",
    "aws-ec2-customergateway.json",
    "aws-ec2-dhcpoptions.json",
    "aws-ec2-ec2fleet.json",
    "aws-ec2-egressonlyinternetgateway.json",
    "aws-ec2-eip.json",
    "aws-ec2-eipassociation.json",
    "aws-ec2-flowlog.json",
    "aws-ec2-gatewayroutetableassociation.json",
    "aws-ec2-instance.json",
    "aws-ec2-internetgateway.json",
    "aws-ec2-ipam.json",
    "aws-ec2-ipamallocation.json",
    "aws-ec2-ipampool.json",
    "aws-ec2-ipampoolcidr.json",
    "aws-ec2-ipamresourcediscovery.json",
    "aws-ec2-ipamresourcediscoveryassociation.json",
    "aws-ec2-ipamscope.json",
    "aws-ec2-keypair.json",
    "aws-ec2-launchtemplate.json",
    "aws-ec2-natgateway.json",
    "aws-ec2-networkacl.json",
    "aws-ec2-networkaclentry.json",
    "aws-ec2-networkinterface.json",
    "aws-ec2-networkinterfaceattachment.json",
    "aws-ec2-placementgroup.json",
    "aws-ec2-prefixlist.json",
    "aws-ec2-route.json",
    "aws-ec2-routetable.json",
    "aws-ec2-securitygroup.json",
    "aws-ec2-securitygroupegress.json",
    "aws-ec2-securitygroupingress.json",
    "aws-ec2-snapshotblockpublicaccess.json",
    "aws-ec2-spotfleet.json",
    "aws-ec2-subnet.json",
    "aws-ec2-subnetroutetableassociation.json",
    "aws-ec2-trafficmirrorfilter.json",
    "aws-ec2-trafficmirrorfilterrule.json",
    "aws-ec2-trafficmirrortarget.json",
    "aws-ec2-transitgateway.json",
    "aws-ec2-transitgatewayattachment.json",
    "aws-ec2-transitgatewayconnect.json",
    "aws-ec2-transitgatewaymulticastdomain.json",
    "aws-ec2-transitgatewaymulticastdomainassociation.json",
    "aws-ec2-transitgatewaymulticastgroupmember.json",
    "aws-ec2-transitgatewaymulticastgroupsource.json",
    "aws-ec2-transitgatewaypeeringattachment.json",
    "aws-ec2-transitgatewayroute.json",
    "aws-ec2-transitgatewayroutetableassociation.json",
    "aws-ec2-transitgatewayroutetablepropagation.json",
    "aws-ec2-transitgatewayvpcattachment.json",
    "aws-ec2-vpc.json",
    "aws-ec2-vpcdhcpoptionsassociation.json",
    "aws-ec2-vpcendpoint.json",
    "aws-ec2-vpcendpointconnectionnotification.json",
    "aws-ec2-vpcendpointservice.json",
    "aws-ec2-vpcendpointservicepermissions.json",
    "aws-ec2-vpcpeeringconnection.json",
    "aws-ec2-vpnconnectionroute.json",
    "aws-ec2-vpngateway.json",
    "aws-ec2-vpngatewayroutepropagation.json",
    "aws-ecr-pullthroughcacherule.json",
    "aws-ecr-registrypolicy.json",
    "aws-ecr-replicationconfiguration.json",
    "aws-ecr-repository.json",
    "aws-ecr-repositorycreationtemplate.json",
    "aws-ecs-capacityprovider.json",
    "aws-ecs-cluster.json",
    "aws-ecs-clustercapacityproviderassociations.json",
    "aws-ecs-primarytaskset.json",
    "aws-ecs-taskdefinition.json",
    "aws-efs-accesspoint.json",
    "aws-efs-filesystem.json",
    "aws-efs-mounttarget.json",
    "aws-eks-accessentry.json",
    "aws-eks-addon.json",
    "aws-eks-fargateprofile.json",
    "aws-eks-identityproviderconfig.json",
    "aws-eks-nodegroup.json",
    "aws-eks-podidentityassociation.json",
    "aws-elasticache-cachecluster.json",
    "aws-elasticache-parametergroup.json",
    "aws-elasticache-replicationgroup.json",
    "aws-elasticache-securitygroup.json",
    "aws-elasticache-securitygroupingress.json",
    "aws-elasticache-serverlesscache.json",
    "aws-elasticache-user.json",
    "aws-elasticache-usergroup.json",
    "aws-elasticloadbalancing-loadbalancer.json",
    "aws-elasticloadbalancingv2-listener.json",
    "aws-elasticloadbalancingv2-listenercertificate.json",
    "aws-elasticloadbalancingv2-listenerrule.json",
    "aws-elasticloadbalancingv2-loadbalancer.json",
    "aws-elasticloadbalancingv2-targetgroup.json",
    "aws-elasticsearch-domain.json",
    "aws-emr-cluster.json",
    "aws-emr-instancefleetconfig.json",
    "aws-emr-instancegroupconfig.json",
    "aws-events-eventbus.json",
    "aws-events-eventbuspolicy.json",
    "aws-events-rule.json",
    "aws-fms-notificationchannel.json",
    "aws-fms-policy.json",
    "aws-fsx-datarepositoryassociation.json",
    "aws-fsx-filesystem.json",
    "aws-fsx-snapshot.json",
    "aws-fsx-storagevirtualmachine.json",
    "aws-fsx-volume.json",
    "aws-globalaccelerator-accelerator.json",
    "aws-globalaccelerator-crossaccountattachment.json",
    "aws-globalaccelerator-endpointgroup.json",
    "aws-globalaccelerator-listener.json",
    "aws-glue-classifier.json",
    "aws-glue-connection.json",
    "aws-glue-crawler.json",
    "aws-glue-customentitytype.json",
    "aws-glue-database.json",
    "aws-glue-datacatalogencryptionsettings.json",
    "aws-glue-dataqualityruleset.json",
    "aws-glue-devendpoint.json",
    "aws-glue-job.json",
    "aws-glue-mltransform.json",
    "aws-glue-partition.json",
    "aws-glue-securityconfiguration.json",
    "aws-glue-table.json",
    "aws-glue-trigger.json",
    "aws-glue-workflow.json",
    "aws-guardduty-filter.json",
    "aws-guardduty-ipset.json",
    "aws-guardduty-malwareprotectionplan.json",
    "aws-guardduty-master.json",
    "aws-guardduty-member.json",
    "aws-guardduty-threatintelset.json",
    "aws-iam-grouppolicy.json",
    "aws-iam-oidcprovider.json",
    "aws-iam-rolepolicy.json",
    "aws-iam-samlprovider.json",
    "aws-iam-servercertificate.json",
    "aws-iam-servicelinkedrole.json",
    "aws-iam-userpolicy.json",
    "aws-iam-usertogroupaddition.json",
    "aws-identitystore-group.json",
    "aws-identitystore-groupmembership.json",
    "aws-imagebuilder-component.json",
    "aws-imagebuilder-containerrecipe.json",
    "aws-imagebuilder-distributionconfiguration.json",
    "aws-imagebuilder-image.json",
    "aws-imagebuilder-imagepipeline.json",
    "aws-imagebuilder-imagerecipe.json",
    "aws-imagebuilder-infrastructureconfiguration.json",
    "aws-imagebuilder-workflow.json",
    "aws-kinesisanalyticsv2-application.json",
    "aws-kinesisfirehose-deliverystream.json",
    "aws-kms-alias.json",
    "aws-kms-key.json",
    "aws-kms-replicakey.json",
    "aws-lakeformation-datacellsfilter.json",
    "aws-lakeformation-datalakesettings.json",
    "aws-lakeformation-permissions.json",
    "aws-lakeformation-principalpermissions.json",
    "aws-lakeformation-resource.json",
    "aws-lakeformation-tag.json",
    "aws-lakeformation-tagassociation.json",
    "aws-lambda-alias.json",
    "aws-lambda-eventinvokeconfig.json",
    "aws-lambda-eventsourcemapping.json",
    "aws-lambda-function.json",
    "aws-lambda-layerversion.json",
    "aws-lambda-layerversionpermission.json",
    "aws-lambda-permission.json",
    "aws-lambda-version.json",
    "aws-logs-accountpolicy.json",
    "aws-logs-delivery.json",
    "aws-logs-deliverydestination.json",
    "aws-logs-deliverysource.json",
    "aws-logs-destination.json",
    "aws-logs-loggroup.json",
    "aws-logs-logstream.json",
    "aws-logs-metricfilter.json",
    "aws-logs-querydefinition.json",
    "aws-logs-resourcepolicy.json",
    "aws-logs-subscriptionfilter.json",
    "aws-msk-batchscramsecret.json",
    "aws-msk-cluster.json",
    "aws-msk-clusterpolicy.json",
    "aws-msk-configuration.json",
    "aws-msk-vpcconnection.json",
    "aws-mwaa-environment.json",
    "aws-networkfirewall-firewall.json",
    "aws-networkfirewall-loggingconfiguration.json",
    "aws-networkfirewall-rulegroup.json",
    "aws-networkfirewall-tlsinspectionconfiguration.json",
    "aws-networkmanager-connectattachment.json",
    "aws-networkmanager-connectpeer.json",
    "aws-networkmanager-corenetwork.json",
    "aws-networkmanager-customergatewayassociation.json",
    "aws-networkmanager-device.json",
    "aws-networkmanager-globalnetwork.json",
    "aws-networkmanager-link.json",
    "aws-networkmanager-linkassociation.json",
    "aws-networkmanager-site.json",
    "aws-networkmanager-sitetositevpnattachment.json",
    "aws-networkmanager-transitgatewaypeering.json",
    "aws-networkmanager-transitgatewayregistration.json",
    "aws-networkmanager-transitgatewayroutetableattachment.json",
    "aws-networkmanager-vpcattachment.json",
    "aws-oam-link.json",
    "aws-oam-sink.json",
    "aws-opensearchservice-domain.json",
    "aws-opsworks-app.json",
    "aws-opsworks-elasticloadbalancerattachment.json",
    "aws-opsworks-userprofile.json",
    "aws-opsworks-volume.json",
    "aws-organizations-account.json",
    "aws-organizations-organization.json",
    "aws-organizations-organizationalunit.json",
    "aws-organizations-policy.json",
    "aws-organizations-resourcepolicy.json",
    "aws-pcaconnectorscep-challenge.json",
    "aws-pcaconnectorscep-connector.json",
    "aws-ram-permission.json",
    "aws-ram-resourceshare.json",
    "aws-rds-dbclusterparametergroup.json",
    "aws-rds-dbinstance.json",
    "aws-rds-dbparametergroup.json",
    "aws-rds-dbproxy.json",
    "aws-rds-dbproxyendpoint.json",
    "aws-rds-dbproxytargetgroup.json",
    "aws-rds-dbsecuritygroup.json",
    "aws-rds-dbsecuritygroupingress.json",
    "aws-rds-eventsubscription.json",
    "aws-rds-integration.json",
    "aws-rds-optiongroup.json",
    "aws-redshift-cluster.json",
    "aws-redshift-clusterparametergroup.json",
    "aws-redshift-clustersecuritygroup.json",
    "aws-redshift-clustersecuritygroupingress.json",
    "aws-redshift-clustersubnetgroup.json",
    "aws-redshift-endpointaccess.json",
    "aws-redshift-endpointauthorization.json",
    "aws-redshift-eventsubscription.json",
    "aws-redshift-scheduledaction.json",
    "aws-resourceexplorer2-defaultviewassociation.json",
    "aws-resourceexplorer2-index.json",
    "aws-resourceexplorer2-view.json",
    "aws-resourcegroups-group.json",
    "aws-rolesanywhere-crl.json",
    "aws-rolesanywhere-profile.json",
    "aws-rolesanywhere-trustanchor.json",
    "aws-route53-dnssec.json",
    "aws-route53-keysigningkey.json",
    "aws-route53-recordset.json",
    "aws-route53-recordsetgroup.json",
    "aws-route53profiles-profile.json",
    "aws-route53profiles-profileassociation.json",
    "aws-route53profiles-profileresourceassociation.json",
    "aws-route53resolver-firewalldomainlist.json",
    "aws-route53resolver-firewallrulegroup.json",
    "aws-route53resolver-firewallrulegroupassociation.json",
    "aws-route53resolver-resolverconfig.json",
    "aws-route53resolver-resolverdnssecconfig.json",
    "aws-route53resolver-resolverendpoint.json",
    "aws-route53resolver-resolverqueryloggingconfig.json",
    "aws-route53resolver-resolverqueryloggingconfigassociation.json",
    "aws-route53resolver-resolverruleassociation.json",
    "aws-s3-accesspoint.json",
    "aws-s3-bucket.json",
    "aws-s3-bucketpolicy.json",
    "aws-s3objectlambda-accesspoint.json",
    "aws-s3objectlambda-accesspointpolicy.json",
    "aws-sagemaker-mlflowtrackingserver.json",
    "aws-sagemaker-modelcard.json",
    "aws-sagemaker-modelpackage.json",
    "aws-sagemaker-modelpackagegroup.json",
    "aws-sdb-domain.json",
    "aws-secretsmanager-resourcepolicy.json",
    "aws-secretsmanager-rotationschedule.json",
    "aws-secretsmanager-secret.json",
    "aws-securityhub-automationrule.json",
    "aws-securityhub-delegatedadmin.json",
    "aws-securityhub-hub.json",
    "aws-securityhub-insight.json",
    "aws-securityhub-organizationconfiguration.json",
    "aws-securityhub-productsubscription.json",
    "aws-securityhub-securitycontrol.json",
    "aws-securityhub-standard.json",
    "aws-servicecatalogappregistry-application.json",
    "aws-servicecatalogappregistry-attributegroup.json",
    "aws-servicecatalogappregistry-attributegroupassociation.json",
    "aws-servicecatalogappregistry-resourceassociation.json",
    "aws-servicediscovery-httpnamespace.json",
    "aws-servicediscovery-instance.json",
    "aws-servicediscovery-privatednsnamespace.json",
    "aws-servicediscovery-publicdnsnamespace.json",
    "aws-servicediscovery-service.json",
    "aws-shield-drtaccess.json",
    "aws-shield-proactiveengagement.json",
    "aws-shield-protection.json",
    "aws-shield-protectiongroup.json",
    "aws-sns-subscription.json",
    "aws-sns-topic.json",
    "aws-sns-topicinlinepolicy.json",
    "aws-sns-topicpolicy.json",
    "aws-sqs-queue.json",
    "aws-sqs-queueinlinepolicy.json",
    "aws-sqs-queuepolicy.json",
    "aws-ssm-association.json",
    "aws-ssm-document.json",
    "aws-ssm-maintenancewindow.json",
    "aws-ssm-maintenancewindowtarget.json",
    "aws-ssm-maintenancewindowtask.json",
    "aws-ssm-parameter.json",
    "aws-ssm-patchbaseline.json",
    "aws-ssm-resourcedatasync.json",
    "aws-sso-application.json",
    "aws-sso-applicationassignment.json",
    "aws-sso-assignment.json",
    "aws-sso-instance.json",
    "aws-sso-instanceaccesscontrolattributeconfiguration.json",
    "aws-sso-permissionset.json",
    "aws-stepfunctions-activity.json",
    "aws-stepfunctions-statemachine.json",
    "aws-stepfunctions-statemachinealias.json",
    "aws-stepfunctions-statemachineversion.json",
    "aws-synthetics-canary.json",
    "aws-transfer-agreement.json",
    "aws-transfer-certificate.json",
    "aws-transfer-connector.json",
    "aws-transfer-profile.json",
    "aws-transfer-server.json",
    "aws-transfer-user.json",
    "aws-transfer-workflow.json",
    "aws-verifiedpermissions-policy.json",
    "aws-verifiedpermissions-policystore.json",
    "aws-verifiedpermissions-policytemplate.json",
    "aws-waf-bytematchset.json",
    "aws-waf-sqlinjectionmatchset.json",
    "aws-wafv2-ipset.json",
    "aws-wafv2-loggingconfiguration.json",
    "aws-wafv2-regexpatternset.json",
    "aws-wafv2-rulegroup.json",
    "aws-wafv2-webacl.json",
    "aws-wafv2-webaclassociation.json",
    "aws-workspaces-workspace.json",
    "aws-xray-group.json",
    "aws-xray-resourcepolicy.json",
    "aws-xray-samplingrule.json",
    "module.json",
]
