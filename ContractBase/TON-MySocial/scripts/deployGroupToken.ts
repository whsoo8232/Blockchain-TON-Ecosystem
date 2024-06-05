import { toNano } from '@ton/core';
import { GroupToken } from '../wrappers/GroupToken';
import { NetworkProvider } from '@ton/blueprint';

export async function run(provider: NetworkProvider) {
    const groupToken = provider.open(await GroupToken.fromInit(BigInt(Math.floor(Math.random() * 10000))));

    await groupToken.send(
        provider.sender(),
        {
            value: toNano('0.05'),
        },
        {
            $$type: 'Deploy',
            queryId: 0n,
        }
    );

    await provider.waitForDeploy(groupToken.address);

    console.log('ID', await groupToken.getId());
}
